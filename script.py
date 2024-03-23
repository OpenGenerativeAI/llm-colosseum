import diambra.arena
from diambra.arena import SpaceTypes, EnvironmentSettingsMultiAgent
from agent import Robot
from eval.game import Game


def main():
    # Environment Settings
    # Environment Settings

    game = Game(
        render=True,
        splash_screen=True,
        characters=["Ryu", "Ken"],
        outfits=[2, 2],
        render_mode="human",
        seed=42,
    )

    game.run()


if __name__ == "__main__":
    main()
