import sys

from dotenv import load_dotenv
from eval.game import Game, Player1, Player2
from loguru import logger

logger.remove()
logger.add(sys.stdout, level="INFO")

load_dotenv()


def main():
    # Environment Settings

    game = Game(
        render=True,
        save_game=True,
        player_1=Player1(
            nickname="Baby",
            model="ollama:mistral",
            robot_type="text",  # vision or text
            temperature=0.7,
        ),
        player_2=Player2(
            nickname="Daddy",
            model="ollama:mistral",
            robot_type="text",
            temperature=0.7,
        ),
    )

    game.run()
    return 0


if __name__ == "__main__":
    main()
