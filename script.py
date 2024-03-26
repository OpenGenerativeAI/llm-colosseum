import sys

from dotenv import load_dotenv
from eval.game import Game, Player1, Player2, generate_random_model
from loguru import logger

logger.remove()
logger.add(sys.stdout, level="INFO")

load_dotenv()


def main():
    # Environment Settings
    game = Game(
        render=True,
        player_1=Player1(
            nickname="Daddy",
            model=generate_random_model(mistral=True),
        ),
        player_2=Player2(
            nickname="Baby",
            model=generate_random_model(openai=True),
        ),
    )
    return game.run()


if __name__ == "__main__":
    main()
