from dotenv import load_dotenv
from eval.game import Game
import sys
import time
from eval.result import display_win_screen

from loguru import logger

logger.remove()  # remove the old handler. Else, the old one will work along with the new one you've added below'
logger.add(sys.stdout, level="INFO")

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
