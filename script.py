from dotenv import load_dotenv
from eval.game import Game
import time
from eval.result import display_win_screen

load_dotenv()


def main():
    # Environment Settings
    # Environment Settings

    game = Game(
        render=True,
        save_game=True,
    )

    game.run()
    display_win_screen()

    time.sleep(10)


if __name__ == "__main__":
    main()
