from dotenv import load_dotenv
from eval.game import Game

import sys

from loguru import logger

logger.remove()  # remove the old handler. Else, the old one will work along with the new one you've added below'
logger.add(sys.stdout, level="INFO")

load_dotenv()


def main():
    # Environment Settings
    # Environment Settings
    while True:
        game = Game(render=True, save_game=True, openai=True)

        game.run()


if __name__ == "__main__":
    main()
