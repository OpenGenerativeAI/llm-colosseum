from dotenv import load_dotenv
from eval.game import Game, Player1, Player2

import sys

from loguru import logger

logger.remove()  # remove the old handler. Else, the old one will work along with the new one you've added below'
logger.add(sys.stdout, level="INFO")

load_dotenv()


def main():
    # Environment Settings
    # Environment Settings
    player1 = Player1(
        nickname="Baby",
        model="mistral:mistral-small-latest",
    )
    player2 = Player2(
        nickname="Daddy",
        model="mistral:mistral-small-latest",
    )

    game = Game(
        render=True,
        save_game=True,
        player_1=player1,
        player_2=player2,
    )

    game.run()
    return 0


if __name__ == "__main__":
    main()
