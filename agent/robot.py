import abc
from collections import defaultdict
import numpy as np
from typing import Dict, List, Optional, Literal
from gymnasium import spaces
from loguru import logger

from .observer import detect_position_from_color, KEN_RED, KEN_GREEN
from .actions import get_actions_from_llm

from .config import (
    MOVES,
    INDEX_TO_MOVE,
    X_SIZE,
    Y_SIZE,
    NB_FRAME_WAIT,
    COMBOS,
    META_INSTRUCTIONS,
)


class Robot:
    observations: List[Optional[dict]] = None  # memory
    next_steps: List[int]  # action plan
    actions: dict  # actions of the agents during a step of the game
    # actions of the agents during the previous step of the game
    previous_actions: Dict[str, List[int]]
    reward: float  # reward of the agent

    action_space: spaces.Space
    character: Optional[str] = None  # character name
    side: int  # side of the stage where playing: 0 = left, 1 = right
    current_direction: Literal["Left", "Right"]  # current direction facing
    sleepy: Optional[bool] = False  # if the robot is sleepy
    only_punch: Optional[bool] = False  # if the robot only punch

    model: str  # model of the robot

    def __init__(
        self,
        action_space: spaces.Space,
        character: str,
        side: int,
        character_color: list,
        ennemy_color: list,
        sleepy: bool = False,
        only_punch: bool = False,
        model: str = "mistral:mistral-large-latest",
    ):
        self.action_space = action_space
        self.character = character
        if side == 0:
            self.current_direction = "Right"
        elif side == 1:
            self.current_direction = "Left"

        self.observations = []
        self.next_steps = []
        self.character_color = character_color
        self.ennemy_color = ennemy_color
        self.side = side
        self.sleepy = sleepy
        self.only_punch = only_punch
        self.model = model
        self.previous_actions = defaultdict(list)
        self.actions = {}

    def act(self) -> int:
        """
        At each game frame, we execute the first action in the list of next steps.

        An action is an integer from 0 to 18, where 0 is no action.

        See the MOVES dictionary for the mapping of actions to moves.
        """
        if not self.next_steps or len(self.next_steps) == 0:
            return 0  # No move

        if self.sleepy:
            return 0

        if self.only_punch:
            # Do a Hadouken
            if self.current_direction == "Right":
                self.next_steps.extend(
                    [
                        MOVES["Down"],
                        MOVES["Right+Down"],
                        MOVES["Right"],
                        MOVES["High Punch"],
                    ]
                )
            elif self.current_direction == "Left":
                self.next_steps.extend(
                    [
                        MOVES["Down"],
                        MOVES["Down+Left"],
                        MOVES["Left"],
                        MOVES["High Punch"],
                    ]
                )

        next_step = self.next_steps.pop(0)

        # Keep track of the current direction
        if "Left" in INDEX_TO_MOVE[next_step]:
            self.current_direction = "Left"
        elif "Right" in INDEX_TO_MOVE[next_step]:
            self.current_direction = "Right"

        return next_step

    def plan(self) -> None:
        """
        The robot will plan its next steps by calling this method.

        In SF3, moves are based on combos, which are list of actions that must be executed in a sequence.

        Moves of Ken
        https://www.eventhubs.com/guides/2009/may/11/ken-street-fighter-3-third-strike-character-guide/

        Moves of Ryu
        https://www.eventhubs.com/guides/2008/may/09/ryu-street-fighter-3-third-strike-character-guide/
        """

        # Detect own position
        own_position = self.observations[-1]["character_position"]
        ennemy_position = self.observations[-1]["ennemy_position"]

        # Note: at the beginning of the game, the position is None

        # If we already have a next step, we don't need to plan
        if len(self.next_steps) > 0:
            return

        # Get the context
        context = self.context_prompt()

        logger.debug(f"Context: {context}")

        # Call the LLM to get the next steps
        next_steps_from_llm = get_actions_from_llm(
            context,
            self.character,
            model=self.model,
            temperature=0.7,
        )

        # Add some steps where we just wait
        next_steps_from_llm.extend([0] * NB_FRAME_WAIT)

        self.next_steps.extend(next_steps_from_llm)

    def observe(self, observation: dict, actions: dict, reward: float):
        """
        The robot will observe the environment by calling this method.

        The latest observations are at the end of the list.
        """

        # detect the position of characters and ennemy based on color
        observation["character_position"] = detect_position_from_color(
            observation, self.character_color
        )
        observation["ennemy_position"] = detect_position_from_color(
            observation, self.ennemy_color
        )

        self.observations.append(observation)
        # we delete the oldest observation if we have more than 10 observations
        if len(self.observations) > 10:
            self.observations.pop(0)

        self.reward = reward

        if actions.get("agent_0") is not None and actions.get("agent_0") != 0:
            self.previous_actions["agent_0"].append(actions["agent_0"])
        if actions.get("agent_1") is not None and actions.get("agent_1") != 0:
            self.previous_actions["agent_1"].append(actions["agent_1"])

        for key, value in actions.items():
            if len(self.previous_actions[key]) > 10:
                self.previous_actions[key].pop(0)

    def context_prompt(self):
        """
        Return a str of the context

        "The observation for you is Left"
        "The observation for the opponent is Left+Up"
        "The action history is Up"
        """


        # Create the position prompt
        side = self.side
        obs_own = self.observations[-1]["character_position"]
        obs_opp = self.observations[-1]["ennemy_position"]

        if obs_own is not None and obs_opp is not None:
            relative_position = np.array(obs_own) - np.array(obs_opp)
            normalized_relative_position = [
                relative_position[0] / X_SIZE,
                relative_position[1] / Y_SIZE,
            ]
        else:
            normalized_relative_position = [0.3, 0]

        position_prompt = ""
        if abs(normalized_relative_position[0]) > 0.1:
            position_prompt += "You are very far from the opponent."
            if normalized_relative_position[0] < 0:
                position_prompt += (
                    "Your opponent is on the right. Move towards the opponent. You need to move to the right."
                )
            else:
                position_prompt += (
                    "Your opponent is on the left. Move towards the opponent. You need to move to the left."
                )

        else:
            position_prompt += "You are close to the opponent. You need to attack him."

        # Create the last action prompt
        last_action_prompt = ""
        if len(self.previous_actions.keys()) >= 0:
            act_own_list = self.previous_actions["agent_" + str(side)]
            act_opp_list = self.previous_actions["agent_" + str(abs(1 - side))]

            if len(act_own_list) == 0:
                act_own = 0
            else:
                act_own = act_own_list[-1]
            if len(act_opp_list) == 0:
                act_opp = 0
            else:
                act_opp = act_opp_list[-1]

            str_act_own = INDEX_TO_MOVE[act_own]
            str_act_opp = INDEX_TO_MOVE[act_opp]

            last_action_prompt += f"Your last action was {str_act_own}. The opponent's last action was {str_act_opp}."


        reward = self.reward

        # Create the score prompt
        score_prompt = ""
        if reward > 0:
            score_prompt += "You are winning. Keep attacking the opponent."
        elif reward < 0:
            score_prompt += "You are losing. Continue to attack the opponent but don't get hit."

        # Assemble everything
        context = f"""{position_prompt}
{last_action_prompt}
Your current score is {reward}. {score_prompt}
To increase your score, attack the opponent. To prevent your score from decreasing, don't get hit by the opponent.
"""

        return context
