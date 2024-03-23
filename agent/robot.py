from typing import List, Optional, Literal
from gymnasium import spaces

MOVES = {
    "No-Move": 0,
    "Left": 1,
    "Left+Up": 2,
    "Up": 3,
    "Up+Right": 4,
    "Right": 5,
    "Right+Down": 6,
    "Down": 7,
    "Down+Left": 8,
    "Low Punch": 9,
    "Medium Punch": 10,
    "High Punch": 11,
    "Low Kick": 12,
    "Medium Kick": 13,
    "High Kick": 14,
    "Low Punch+Low Kick": 15,
    "Medium Punch+Medium Kick": 16,
    "High Punch+High Kick": 17,
}
INDEX_TO_MOVE = {v: k for k, v in MOVES.items()}


class Robot:
    observations: List[Optional[dict]] = None  # memory
    next_steps: List[int] = []  # action plan

    action_space: spaces.Space
    character: Optional[str] = None  # character name
    side: int  # side of the stage where playing: 0 = left, 1 = right
    current_direction: Literal["Left", "Right"]  # current direction facing

    def __init__(self, action_space: spaces.Space, character: str, side: int):
        self.action_space = action_space
        self.character = character
        if side == 0:
            self.current_direction = "Right"
        elif side == 1:
            self.current_direction = "Left"

        self.observations = []

    def act(self) -> int:
        """
        At each game frame, we execute the first action in the list of next steps.

        An action is an integer from 0 to 18, where 0 is no action.

        See the MOVES dictionary for the mapping of actions to moves.
        """
        if not self.next_steps or len(self.next_steps) == 0:
            return 0  # No move

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
        # Just add a random action to the next steps
        # self.next_steps.append(self.action_space.sample())
        if len(self.next_steps) > 0:
            return

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
                    MOVES["Left+Down"],
                    MOVES["Left"],
                    MOVES["High Punch"],
                ]
            )

    def observe(self, observation: dict):
        """
        The robot will observe the environment by calling this method.

        The latest observations are at the end of the list.
        """
        self.observations.append(observation)
        # we delete the oldest observation if we have more than 10 observations
        if len(self.observations) > 10:
            self.observations.pop(0)
