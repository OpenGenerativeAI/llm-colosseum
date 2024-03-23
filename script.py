from eval.game import Game
from dotenv import load_dotenv

load_dotenv()


def main():
    # Environment Settings
    # Environment Settings

    game = Game(
        render=True,
    )

    game.run()


if __name__ == "__main__":
    main()
