import sys

from dotenv import load_dotenv
from eval.game import Game, Player1, Player2
from loguru import logger

logger.remove()
logger.add(sys.stdout, level="INFO")

load_dotenv()

li_models = [
    "openai:gpt-4o",
    "mistral:pixtral-12b-2409",
    "openai:gpt-4o-mini",
]


# Starting with vision tournamennt
def main(model_1: str, model_2: str):
    # Environment Settings
    game = Game(
        render=True,
        player_1=Player1(
            nickname="Daddy",
            model=model_1,
            robot_type="vision",  # vision or text
            temperature=0.7,
        ),
        player_2=Player2(
            nickname="Baby",
            model=model_2,
            robot_type="vision",
            temperature=0.7,
        ),
    )
    return game.run()


if __name__ == "__main__":
    for i in range(10):
        for j in range(10):
            model_1 = li_models[i % len(li_models)]
            model_2 = li_models[j % len(li_models)]
        main(model_1=model_1, model_2=model_2)
