import datetime
import os
import random
import traceback
from threading import Thread
from typing import List, Optional

from agent import KEN_GREEN, KEN_RED, Robot
from agent.config import MODELS
from diambra.arena import (
    EnvironmentSettingsMultiAgent,
    RecordingSettings,
    SpaceTypes,
    make,
)
from rich import print


def generate_random_model(openai: bool = False, mistral: bool = True):
    models_available = []

    for model, models in MODELS.items():
        if openai and model == "OPENAI":
            models_available.extend(models)
        if mistral and model == "MISTRAL":
            models_available.extend(models)

    random.seed()
    # Generate a pair of random two models
    random_model = random.choice(models_available)

    return random_model


class Player:
    nickname: str
    model: str
    robot: Optional[Robot] = None
    temperature: Optional[float] = 0.0

    def verify_provider_name(self):
        if self.model.startswith("openai"):
            assert (
                os.environ.get("OPENAI_API_KEY") is not None
            ), "OpenAI API key not set"
        if self.model.startswith("mistral"):
            assert (
                os.environ.get("MISTRAL_API_KEY") is not None
            ), "Mistral API key not set"


class Player1(Player):
    def __init__(
        self,
        nickname: str,
        model: str,
    ):
        self.nickname = nickname
        self.model = model
        self.robot = Robot(
            action_space=None,
            character="Ken",
            side=0,
            character_color=KEN_RED,
            ennemy_color=KEN_GREEN,
            only_punch=os.getenv("TEST_MODE", False),
            model=self.model,
            player_nb=1,
        )
        print(f"[red] Player 1 using: {self.model}")
        self.verify_provider_name()


class Player2(Player):
    def __init__(
        self,
        nickname: str,
        model: str,
    ):
        self.nickname = nickname
        self.model = model
        self.robot = Robot(
            action_space=None,
            character="Ken",
            side=1,
            character_color=KEN_GREEN,
            ennemy_color=KEN_RED,
            sleepy=os.getenv("TEST_MODE", False),
            model=self.model,
            player_nb=2,
        )
        print(f"[green] Player 2 using: {self.model}")
        self.verify_provider_name()


class Episode:
    player_1: Optional[Player1]
    player_2: Player2
    player_1_won: Optional[bool] = None

    def __init__(self, player_1: Optional[Player1], player_2: Player2):
        self.player_1 = player_1
        self.player_2 = player_2

    def save(self):
        if self.player_1 is None:
            # Playing with the controller
            # Results are not saved
            return

        # Write the results to an existing csv with headers "player_1", "player_2", "winner"
        timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")

        # Verifty if the file exists
        if not os.path.exists("results.csv"):
            with open("results.csv", "w") as f:
                f.write(
                    "id,player_1_model,player_1_temperature,player_2_model,player_2_temperature,player_1_won\n"
                )

        with open("results.csv", "a") as f:
            f.write(
                f"{timestamp},{self.player_1.model},{self.player_1.temperature},"
                + f"{self.player_2.model},{self.player_2.temperature},{self.player_1_won}\n"
            )


class Game:
    player_1: Optional[Player1] = None  # First player. None if Human
    player_2: Player2

    render: Optional[bool] = False
    splash_screen: Optional[bool] = False
    save_game: Optional[bool] = False
    characters: Optional[List[str]] = ["Ken", "Ken"]
    outfits: Optional[List[int]] = [1, 3]
    frame_shape: Optional[List[int]] = [0, 0, 0]
    seed: Optional[int] = 42
    settings: EnvironmentSettingsMultiAgent = None  # Settings of the game
    env = None  # Environment of the game

    def __init__(
        self,
        player_1: Optional[Player1],
        player_2: Player2,
        render: bool = False,
        save_game: bool = False,
        splash_screen: bool = False,
        characters: List[str] = ["Ken", "Ken"],
        super_arts: List[int] = [3, 3],
        outfits: List[int] = [1, 3],
        frame_shape: List[int] = [0, 0, 0],
        seed: int = 42,
    ):
        """_summary_

        Args:
            render (bool, optional): Renders the fights. Defaults to False.
            splash_screen (bool, optional): Display the splash screen. Defaults to False.
            characters (List[str], optional): List of the players to have. Defaults to ["Ryu", "Ken"].
            outfits (List[int], optional): Outfits to run. Defaults to [2, 2].
            frame_shape (List[int], optional): Don't know :D . Defaults to [0, 0, 0].
            seed (int, optional): Random seed. Defaults to 42.
        """
        self.render = render
        self.splash_screen = splash_screen
        self.save_game = save_game
        self.characters = characters
        self.super_arts = super_arts
        self.outfits = outfits
        self.frame_shape = frame_shape
        self.seed = seed
        self.settings = self._init_settings()
        self.env = self._init_env(self.settings)
        self.observation, self.info = self.env.reset(seed=self.seed)
        if player_1 is not None:
            self.player_1 = player_1
        else:
            # If player 1 is not provided, we will use the controller
            # The human player will be able to play with the controller
            from diambra.arena.utils.controller import get_diambra_controller

            self.player_1 = None
            self.controller = get_diambra_controller(
                self.env.unwrapped.get_actions_tuples(),
                # force_configure=True,
            )
            self.controller.start()
        self.player_2 = player_2

    def _init_settings(self) -> EnvironmentSettingsMultiAgent:
        """
        Initializes the settings for the game.
        """
        settings = EnvironmentSettingsMultiAgent(
            render_mode="rgb_array",
            splash_screen=self.splash_screen,
        )

        settings.action_space = (SpaceTypes.DISCRETE, SpaceTypes.DISCRETE)
        settings.characters = self.characters
        settings.outfits = self.outfits
        settings.frame_shape = self.frame_shape
        settings.super_art = self.super_arts

        return settings

    def _init_recorder(self) -> RecordingSettings:
        """
        Initializes the recorder for the game.
        """
        if not self.save_game:
            return None
        # Recording settings in root directory
        root_dir = os.path.dirname(os.path.abspath(__file__))
        game_id = "sfiii3n"
        timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        recording_settings = RecordingSettings()
        recording_settings.dataset_path = os.path.join(
            root_dir, "diambra/episode_recording", game_id, "-", timestamp
        )
        recording_settings.username = "llm-colosseum"

        return recording_settings

    def _init_env(self, settings: EnvironmentSettingsMultiAgent):
        """
        Initializes the environment for the game.
        """
        render_mode = "human" if self.render else "rgb_array"
        recorder_settings = self._init_recorder()
        if self.save_game:
            return make(
                "sfiii3n",
                settings,
                render_mode=render_mode,
                episode_recording_settings=recorder_settings,
            )
        return make("sfiii3n", settings, render_mode=render_mode)

    def _save(self):
        """
        Save the game state.
        """
        pass

    def _determine_winner(self, episode: Episode):
        p1_health = self.observation["P1"]["health"][0]
        p2_health = self.observation["P2"]["health"][0]
        if p1_health > p2_health:
            episode.player_1_won = True
        elif p2_health > p1_health:
            episode.player_1_won = False
        else:
            return "Draw"

    def run(self):
        """
        Runs the game with the given settings.
        """
        try:
            self.actions = {
                "agent_0": 0,
                "agent_1": 0,
            }
            self.reward = 0.0

            if self.player_1 is not None:
                self.player_1.robot.observe(self.observation, {}, 0.0)

            self.player_2.robot.observe(self.observation, {}, 0.0)
            # Initialize the episode
            episode = Episode(player_1=self.player_1, player_2=self.player_2)
            # Start the threads that make API calls
            if self.player_1 is not None:
                player1_thread = PlanAndActPlayer1(game=self, episode=episode)
                player1_thread.start()
            player2_thread = PlanAndActPlayer2(game=self, episode=episode)
            player2_thread.start()

            while True:
                # Render the game
                if self.render:
                    self.env.render()

                actions = self.actions

                if self.player_1 is None:
                    # If player 1 is not provided, we use the controller
                    try:
                        # On MacOS we need to install pyobjc
                        # pip install pyobjc
                        # https://stackoverflow.com/questions/76434535/attributeerror-super-object-has-no-attribute-init

                        controller_actions = self.controller.get_actions()
                        actions["agent_1"] = (
                            controller_actions[0] + controller_actions[1]
                        )
                    except Exception as e:
                        print(e)

                if "agent_0" not in actions:
                    actions["agent_0"] = 0
                if "agent_1" not in actions:
                    actions["agent_1"] = 0
                observation, reward, terminated, truncated, info = self.env.step(
                    actions
                )
                # Remove the actions that were executed
                if "agent_0" in self.actions:
                    del actions["agent_0"]
                if "agent_1" in self.actions:
                    del actions["agent_1"]

                self.observation = observation
                self.reward += reward

                p1_wins = observation["P1"]["wins"][0]
                p2_wins = observation["P2"]["wins"][0]

                if p1_wins == 1 or p2_wins == 1:
                    if self.player_1 is not None:
                        player1_thread.running = False
                    player2_thread.running = False
                    episode.player_1_won = p1_wins == 1
                    if episode.player_1_won:
                        print(
                            f"[red] Player1 {self.player_1.robot.model} '{self.player_1.nickname}' won!"
                        )
                    else:
                        print(
                            f"[green] Player2 {self.player_2.robot.model} {self.player_2.nickname} won!"
                        )
                    episode.save()
                    self.env.close()
                    break
        except Exception as e:
            # self.env.close()
            print(f"Exception: {e}")
            traceback.print_exception(limit=10)
            traceback.print_tb(limit=40)
            if self.player_1 is None:
                self.controller.stop()
            self.env.close()
        try:
            if self.player_1 is None:
                self.controller.stop()
            self.env.close()
        except Exception as e:
            pass  # Ignore the exception
        return 0


class PlanAndAct(Thread):
    def __init__(self, game: Game, episode: Episode):
        self.running = True
        self.game = game
        self.episode = episode

        Thread.__init__(self, daemon=True)
        # atexit.register(self.stop)


class PlanAndActPlayer1(PlanAndAct):
    def run(self) -> None:
        while self.running:
            if "agent_0" not in self.game.actions:
                # Plan
                self.game.player_1.robot.plan()
                # Act
                self.game.actions["agent_0"] = self.game.player_1.robot.act()
                # Observe the environment
                self.game.player_1.robot.observe(
                    self.game.observation, self.game.actions, self.game.reward
                )


class PlanAndActPlayer2(PlanAndAct):
    def run(self) -> None:
        while self.running:
            if "agent_1" not in self.game.actions:
                # Plan
                self.game.player_2.robot.plan()
                # Act
                self.game.actions["agent_1"] = self.game.player_2.robot.act()
                # Observe the environment
                self.game.player_2.robot.observe(
                    self.game.observation, self.game.actions, -self.game.reward
                )
