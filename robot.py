from typing import List


class Robot:
    next_steps: List[list] = []  # The next steps of the robots

    def __init__(self, action_space):
        self.action_space = action_space

    def act(self):
        """
        The robot will act every turn by calling this method.
        """
        return self.next_steps.pop(0) if self.next_steps else None

    def plan(self):
        """
        The robot will plan its next steps by calling this method.
        """
        # Just add a random action to the next steps
        self.next_steps.append(self.action_space.sample())
