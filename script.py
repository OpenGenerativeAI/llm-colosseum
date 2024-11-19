import sys

from dotenv import load_dotenv
from eval.game import Game, Player1, Player2
from loguru import logger

logger.remove()
logger.add(sys.stdout, level="INFO")

load_dotenv()


# Starting with vision tournamennt
def main():
    # Environment Settings
    game = Game(
        render=True,
        player_1=Player1(
            nickname="Daddy",
            model="openai:gpt-4o-mini",
            robot_type="text",  # vision or text
            temperature=0.7,
        ),
        player_2=Player2(
            nickname="Baby",
            model="openai:gpt-4o-mini",
            robot_type="text",
            temperature=0.7,
        ),
    )
    return game.run()


if __name__ == "__main__":
    main()
