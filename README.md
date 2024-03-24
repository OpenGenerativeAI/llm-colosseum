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

https://github.com/OpenGenerativeAI/llm-colosseum/assets/19614572/ec3f2d4b-66b8-4e51-9897-cdab3b160025


### 1 VS 1 X 6 : Mistral 7B vs Mistral 7B
https://github.com/OpenGenerativeAI/llm-colosseum/assets/19614572/2935455f-a78c-436c-92df-a3c3d853c1d3



## A new kind of benchmark ? 

Street Fighter III assesses the ability of LLMs to understand their environment and take actions based on a specific context.
As opposed to RL models, which blindly take actions based on the reward function, LLMs are fully aware of the context and act accordingly.

# Results 

Our experimentations (342 fights so far) led to the following leader board. 
Each LLM has an ELO score based on its results 

## Ranking

### ELO ranking

|     | Model                         |  Rating |
| --: | :---------------------------- | ------: |
|   5 | openai:gpt-3.5-turbo-0125     | 1776.11 |
|   0 | mistral:mistral-small-latest  | 1586.16 |
|   6 | openai:gpt-4-1106-preview     | 1584.78 |
|   4 | openai:gpt-4                  |  1517.2 |
|   7 | openai:gpt-4-turbo-preview    | 1509.28 |
|   2 | openai:gpt-4-0125-preview     | 1438.92 |
|   3 | mistral:mistral-medium-latest | 1356.19 |
|   1 | mistral:mistral-large-latest  | 1231.36 |

### Win rate matrix

![Win rate matrix](notebooks/win_rate_matrix.png)


# Explanation

Each player is controlled by an LLM. 
We send to the LLM a text description of the screen. The LLM decide on the next moves its character will make. The next moves depends on its previous moves, the moves of its opponents, its power and health bars. 

- Agent based
- Multithreading
- Real time

# Installation

- Follow instructions in https://docs.diambra.ai/#installation
- Download the ROM and put it in `~/.diambra/roms`
- Install with `pip3 install -r requirements`
- Create a `.env` file and fill it with the content like in the `.env.example` file
- Run with `make run`

## Test mode

To disable the LLM calls, set `DISABLE_LLM` to `True` in the `.env` file.
It will choose the action randomly.

## Positions

- x is between 0 and 384
- y is between 0 and 224

## Logging

Change the logging level in the `script.py` file.



# Credits

Made with ❤️ by the OpenGenerativeAI team @oulianov @Pierre-LouisBJT @Platinn @StanGirard during Mistral Hackathon 2024 in San Francisco
