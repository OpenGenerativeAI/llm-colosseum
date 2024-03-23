from typing import List, Optional
from agent import Robot
from diambra.arena import SpaceTypes, EnvironmentSettingsMultiAgent, make
from context_prompt import context_prompt


class Game:

    render: Optional[bool] = False
    splash_screen: Optional[bool] = False
    characters: Optional[List[str]] = ["Ryu", "Ken"]
    outfits: Optional[List[int]] = [2, 2]
    frame_shape: Optional[List[int]] = [0, 0, 0]
    render_mode: Optional[str] = "human"  # either human or rgb_array
    seed: Optional[int] = 42
    settings: EnvironmentSettingsMultiAgent = None  # Settings of the game
    env = None  # Environment of the game
    agent_1: Robot = None  # First agent
    agent_2: Robot = None  # Second agent

    def __init__(
        self,
        render: bool = False,
        splash_screen: bool = False,
        characters: List[str] = ["Ryu", "Ken"],
        outfits: List[int] = [2, 2],
        frame_shape: List[int] = [0, 0, 0],
        render_mode: str = "human",
        seed: int = 42,
    ):
        """_summary_

        Args:
            render (bool, optional): Renders the fights. Defaults to False.
            splash_screen (bool, optional): Display the splash screen. Defaults to False.
            characters (List[str], optional): List of the players to have. Defaults to ["Ryu", "Ken"].
            outfits (List[int], optional): Outfits to run. Defaults to [2, 2].
            frame_shape (List[int], optional): Don't know :D . Defaults to [0, 0, 0].
            render_mode (str, optional): Weither to display an RGB or not. Defaults to "human".
            seed (int, optional): Random seed. Defaults to 42.
        """
        self.render = render
        self.splash_screen = splash_screen
        self.characters = characters
        self.outfits = outfits
        self.frame_shape = frame_shape
        self.render_mode = render_mode
        self.seed = seed
        self.settings = self._init_settings()
        self.env = self._init_env(self.settings)
        self.observation, self.info = self.env.reset(seed=self.seed)

    def _init_settings(self) -> EnvironmentSettingsMultiAgent:
        """
        Initializes the settings for the game.
        """
        settings = EnvironmentSettingsMultiAgent(
            render_mode=self.render_mode,
            splash_screen=self.splash_screen,
        )

        settings.action_space = (SpaceTypes.DISCRETE, SpaceTypes.DISCRETE)

        settings.characters = self.characters

        settings.outfits = self.outfits

        settings.frame_shape = self.frame_shape

        return settings

    def _init_env(self, settings: EnvironmentSettingsMultiAgent):
        """
        Initializes the environment for the game.
        """
        return make("sfiii3n", settings, render_mode=self.render_mode)

    def run(self):
        """
        Runs the game with the given settings.
        """

        self.agent_1 = Robot(
            action_space=self.env.action_space["agent_0"],
            character="Ryu",
            side=0,
        )

        self.agent_2 = Robot(
            action_space=self.env.action_space["agent_1"],
            character="Ken",
            side=1,
        )

        self.agent_1.observe(self.observation)
        self.agent_2.observe(self.observation)

        while True:
            if self.render:
                self.env.render()

            # Plan
            self.agent_1.plan()
            self.agent_2.plan()

            # Act
            actions = {"agent_0": self.agent_1.act(), "agent_1": self.agent_2.act()}

            print("Actions: {}".format(actions))
            # Execute actions in the game
            observation, reward, terminated, truncated, info = self.env.step(actions)

            done = terminated or truncated
            print("Reward: {}".format(reward))
            print("Done: {}".format(done))
            print("Info: {}".format(info))
            print(context_prompt(self.agent_1, observation, actions))

            if done:
                # Optionally, change episode settings here
                options = {}
                options["characters"] = (None, None)
                options["char_outfits"] = (5, 5)
                observation, info = self.env.reset(options=options)
                break

            # Observe the environment
            self.agent_1.observe(observation)
            self.agent_2.observe(observation)
        self.env.close()
        return 0
