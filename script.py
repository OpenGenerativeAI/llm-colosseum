from dotenv import load_dotenv
from eval.game import Game, Player1

import sys

from loguru import logger

logger.remove()  # remove the old handler. Else, the old one will work along with the new one you've added below'
logger.add(sys.stdout, level="INFO")

load_dotenv()


def main():
    # Environment Settings
    # Environment Settings
    game = Game(render=True, save_game=False, openai=True, 
        player_1 = Player1(
        nickname="Baby",
        model="mistral:mistral-small-latest",
    )
    )

    game.run()
    return 0


if __name__ == "__main__":
    main()

    # pip install pyobjc
    # https://stackoverflow.com/questions/76434535/attributeerror-super-object-has-no-attribute-init
