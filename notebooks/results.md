# Win rate table

|     | model                         | games_won | games_played | win_rate |
| --: | :---------------------------- | --------: | -----------: | -------: |
|   4 | openai:gpt-3.5-turbo-0125     |        31 |           37 | 0.837838 |
|   0 | openai:gpt-4-1106-preview     |        27 |           37 |  0.72973 |
|   6 | mistral:mistral-small-latest  |        51 |           77 | 0.662338 |
|   1 | openai:gpt-4                  |        32 |           54 | 0.592593 |
|   7 | openai:gpt-4-0125-preview     |        16 |           37 | 0.432432 |
|   5 | mistral:mistral-medium-latest |        20 |           74 |  0.27027 |
|   3 | mistral:mistral-large-latest  |        15 |           69 | 0.217391 |

# Results matrix

![Win rate matrix](win_rate_matrix.png)

| model_1                       | mistral:mistral-large-latest | mistral:mistral-medium-latest | mistral:mistral-small-latest | openai:gpt-3.5-turbo-0125 | openai:gpt-4 | openai:gpt-4-0125-preview | openai:gpt-4-1106-preview |
| :---------------------------- | ---------------------------: | ----------------------------: | ---------------------------: | ------------------------: | -----------: | ------------------------: | ------------------------: |
| mistral:mistral-large-latest  |                            1 |                      0.555556 |                            0 |                  0.142857 |            0 |                      0.25 |                      0.25 |
| mistral:mistral-medium-latest |                     0.444444 |                      0.428571 |                        0.625 |                         0 |     0.277778 |                       0.2 |                 0.0666667 |
| mistral:mistral-small-latest  |                            1 |                         0.375 |                     0.615385 |                  0.230769 |     0.764706 |                  0.866667 |                  0.545455 |
| openai:gpt-3.5-turbo-0125     |                     0.857143 |                             1 |                     0.769231 |                         1 |     0.666667 |                       0.5 |                         1 |
| openai:gpt-4                  |                            1 |                      0.722222 |                     0.235294 |                  0.333333 |          0.5 |                       nan |                         0 |
| openai:gpt-4-0125-preview     |                         0.75 |                           0.8 |                     0.133333 |                       0.5 |          nan |                       0.5 |                         0 |
| openai:gpt-4-1106-preview     |                         0.75 |                      0.933333 |                     0.454545 |                         0 |            1 |                         1 |                       nan |
