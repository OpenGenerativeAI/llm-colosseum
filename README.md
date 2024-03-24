# llm-collosseum

Make LLM fight each other in real time in Street Fighter III.

Which LLM will be the best fighter ?


https://github.com/OpenGenerativeAI/llm-colosseum/assets/19614572/ec3f2d4b-66b8-4e51-9897-cdab3b160025


![LLM colosseum](multi_agents.png)



https://github.com/OpenGenerativeAI/llm-colosseum/assets/19614572/2935455f-a78c-436c-92df-a3c3d853c1d3



## Explanation

Each player is controlled by an LLM. 
We send to the LLM a text description of the screen. The LLM decide on the next moves its character will make. The next moves depends on its previous moves, the moves of its opponents, its power and health bars. 

- Agent based
- Multithreading
- Real time

## A new kind of benchmark ? 

Street Fighter III assesses the ability of LLMs to understand their environment and take actions based on a specific context.
As opposed to RL models, which blindly take actions based on the reward function, LLMs are fully aware of the context and act accordingly.

## Results

Our experimentations (342 fights so far) led to the following leader board. 
Each LLM has an ELO score based on its results 

## Installation

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
