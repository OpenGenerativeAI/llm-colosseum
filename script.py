from dotenv import load_dotenv
from eval.game import Game

load_dotenv()


def main():
    # Environment Settings
    # Environment Settings

    game = Game(
        render=True,
        save_game=True,
    )

    game.run()


if __name__ == "__main__":
    main()
