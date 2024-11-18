import sys

from dotenv import load_dotenv
from eval.game import Game, Player1, Player2
from loguru import logger

logger.remove()
logger.add(sys.stdout, level="INFO")

load_dotenv()

li_models = [
    "openai:gpt-4o-mini",
    "anthropic:claude-3-haiku-20240307",
    "openai:gpt-4o",
    "mistral:pixtral-12b-2409",
]


# Starting with vision tournamennt
def main(model_1: str, model_2: str, type_1: str = "vision", type_2: str = "vision"):
    # Environment Settings
    game = Game(
        render=True,
        player_1=Player1(
            nickname="Daddy",
            model=model_1,
            robot_type=type_1,  # vision or text
            temperature=0.7,
        ),
        player_2=Player2(
            nickname="Baby",
            model=model_2,
            robot_type=type_2,
            temperature=0.7,
        ),
    )
    return game.run()


if __name__ == "__main__":
    for i in range(3, 20):
        for j in range(0, 20):
            model_1 = li_models[i % len(li_models)]
            model_2 = li_models[j % len(li_models)]
            main(
                model_1=model_1,
                model_2=model_2,
                type_1="vision" if i % 2 == 0 else "text",
                type_2="vision" if j % 2 == 0 else "text",
            )
