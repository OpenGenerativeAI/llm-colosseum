import sys
from dotenv import load_dotenv
from eval.game import Game, Player1, Player2
from loguru import logger

logger.remove()
logger.add(sys.stdout, level="INFO")

load_dotenv()

# List of models Tested for the leaderboards
li_models = [
    "anthropic:claude-3-sonnet-20240229",
    "mistral:pixtral-large-latest",
    "mistral:pixtral-12b-2409",
    "anthropic:claude-3-haiku-20240307",
    "openai:gpt-4o",
    "openai:gpt-4o-mini",
    "anthropic:claude-3-sonnet-20240229",
]


# Starting with vision tournamennt
def main(
    model_1: str = "openai:gpt-4o-mini",
    model_2: str = "anthropic:claude-3-haiku-20240307",
    type_1: str = "vision",
    type_2: str = "vision",
):
    # Environment Settings
    game = Game(
        render=True,
        player_1=Player1(
            nickname="Daddy",
            model="openai:gpt-4o-mini",
            robot_type="vision",  # "vision" or "text"
            temperature=0.7,
        ),
        player_2=Player2(
            nickname="Baby",
            model="anthropic:claude-3-haiku-20240307",
            robot_type="vision",
            temperature=0.7,
        ),
    )
    return game.run()


if __name__ == "__main__":
    main(
        model_1="openai:gpt-4o-mini",
        model_2="anthropic:claude-3-haiku-20240307",
        type_1="vision",
        type_2="vision",
    )
