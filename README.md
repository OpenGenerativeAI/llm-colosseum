# Evaluate LLMs in real time with Street Fighter III

<div align="center">
    <img src="./logo.png" alt="colosseum-logo" width="30%"  style="border-radius: 50%; padding-bottom: 20px"/>
</div>

Make LLM fight each other in real time in Street Fighter III.

Which LLM will be the best fighter ?

## Our criterias 🔥

They need to be:

- **Fast**: It is a real time game, fast decisions are key
- **Smart**: A good fighter thinks 50 moves ahead
- **Out of the box thinking**: Outsmart your opponent with unexpected moves
- **Adaptable**: Learn from your mistakes and adapt your strategy
- **Resilient**: Keep your RPS high for an entire game

## Let the fight begin 🥷

### 1 VS 1: Mistral 7B vs Mistral 7B

https://github.com/OpenGenerativeAI/llm-colosseum/assets/19614572/79b58e26-7902-4687-af5d-0e1e845ecaf8

### 1 VS 1 X 6 : Mistral 7B vs Mistral 7B

https://github.com/OpenGenerativeAI/llm-colosseum/assets/19614572/5d3d386b-150a-48a5-8f68-7e2954ec18db

## A new kind of benchmark ?

Street Fighter III assesses the ability of LLMs to understand their environment and take actions based on a specific context.
As opposed to RL models, which blindly take actions based on the reward function, LLMs are fully aware of the context and act accordingly.

# Results

Our experimentations (342 fights so far) led to the following leader board.
Each LLM has an ELO score based on its results

## Ranking

### ELO ranking

| Model                          |  Rating |
| ------------------------------ | ------: |
| 🥇openai:gpt-3.5-turbo-0125    | 1776.11 |
| 🥈mistral:mistral-small-latest | 1586.16 |
| 🥉openai:gpt-4-1106-preview    | 1584.78 |
| openai:gpt-4                   |  1517.2 |
| openai:gpt-4-turbo-preview     | 1509.28 |
| openai:gpt-4-0125-preview      | 1438.92 |
| mistral:mistral-medium-latest  | 1356.19 |
| mistral:mistral-large-latest   | 1231.36 |

### Win rate matrix

![Win rate matrix](notebooks/win_rate_matrix.png)

# Explanation

Each player is controlled by an LLM.
We send to the LLM a text description of the screen. The LLM decide on the next moves its character will make. The next moves depends on its previous moves, the moves of its opponents, its power and health bars.

- Agent based
- Multithreading
- Real time

  ![fight3 drawio](https://github.com/OpenGenerativeAI/llm-colosseum/assets/78322686/3a212601-f54c-490d-aeb9-6f7c2401ebe6)

# Installation

- Follow instructions in https://docs.diambra.ai/#installation
- Download the ROM and put it in `~/.diambra/roms`
- (Optional) Create and activate a [new python venv](https://docs.python.org/3/library/venv.html)
- Install dependencies with `make install` or `pip install -r requirements.txt`
- Create a `.env` file and fill it with the content like in the `.env.example` file
- Run with `make run`

## Test mode

To disable the LLM calls, set `DISABLE_LLM` to `True` in the `.env` file.
It will choose the actions randomly.

## Logging

Change the logging level in the `script.py` file.

## Local model

You can run the arena with local models using [Ollama](https://ollama.com/).

1. Make sure you have ollama installed, running, and with a model downloaded (run `ollama serve mistral` in the terminal for example)

2. Run `make local` to start the fight.

By default, it runs mistral against mistral. To use other models, you need to change the parameter model in `ollama.py`.

```python
from eval.game import Game, Player1, Player2

def main():
    game = Game(
        render=True,
        save_game=True,
        player_1=Player1(
            nickname="Baby",
            model="ollama:mistral", # change this
        ),
        player_2=Player2(
            nickname="Daddy",
            model="ollama:mistral", # change this
        ),
    )
    game.run()
    return 0
```

The convention we use is `model_provider:model_name`. If you want to use another local model than Mistral, you can do `ollama:some_other_model`

## How to make my own LLM model play? Can I improve the prompts?

The LLM is called in `Robot.call_llm()` method of the `agent/robot.py` file.

```python
    def call_llm(
        self,
        temperature: float = 0.7,
        max_tokens: int = 50,
        top_p: float = 1.0,
    ) -> str:
        """
        Make an API call to the language model.

        Edit this method to change the behavior of the robot!
        """
        # self.model is a slug like mistral:mistral-small-latest or ollama:mistral
        provider_name, model_name = get_provider_and_model(self.model)
        client = get_sync_client(provider_name) # OpenAI client

        # Generate the prompts
        move_list = "- " + "\n - ".join([move for move in META_INSTRUCTIONS])
        system_prompt = f"""You are the best and most aggressive Street Fighter III 3rd strike player in the world.
Your character is {self.character}. Your goal is to beat the other opponent. You respond with a bullet point list of moves.
{self.context_prompt()}
The moves you can use are:
{move_list}
----
Reply with a bullet point list of moves. The format should be: `- <name of the move>` separated by a new line.
Example if the opponent is close:
- Move closer
- Medium Punch

Example if the opponent is far:
- Fireball
- Move closer"""

        # Call the LLM
        completion = client.chat.completions.create(
            model=model_name,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": "Your next moves are:"},
            ],
            temperature=temperature,
            max_tokens=max_tokens,
            top_p=top_p,
        )

        # Return the string to be parsed with regex
        llm_response = completion.choices[0].message.content.strip()
        return llm_response
```

To use another model or other prompts, make a call to another client in this function, change the system prompt, or make any fancy stuff.

### Submit your model

Create a new class herited from `Robot` that has the changes you want to make and open a PR.

We'll do our best to add it to the ranking!

# Credits

Made with ❤️ by the OpenGenerativeAI team from [phospho](https://phospho.ai) (@oulianov @Pierre-LouisBJT @Platinn) and [Quivr](https://www.quivr.app) (@StanGirard) during Mistral Hackathon 2024 in San Francisco
