from typing import List, Optional

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


class Robot:
    next_steps: List[int] = []  # The next steps of the robots
    observation: Optional[dict] = None  # The observation of the robots
    action_space: Optional[int] = None  # The action space of the robots

    def __init__(self, action_space):
        self.action_space = action_space

    def act(self) -> int:
        """
        The robot will act every turn by calling this method.

        An action is an integer from 0 to 18
        """
        return self.next_steps.pop(0) if self.next_steps else None

    def plan(self):
        """
        The robot will plan its next steps by calling this method.
        """
        # Just add a random action to the next steps
        # self.next_steps.append(self.action_space.sample())
        self.next_steps.extend(
            [
                # Do a Hadouken
                MOVES["Down"],
                MOVES["Down+Right"],
                MOVES["Right"],
                MOVES["High Punch"],
            ]
        )

    def observe(self, observation):
        """
        The robot will observe the environment by calling this method.
        """
        self.observation = observation
