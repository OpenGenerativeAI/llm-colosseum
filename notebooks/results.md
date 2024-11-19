# Elo Score

|     | Model                             |  Rating |
| --: | :-------------------------------- | ------: |
|   3 | openai:gpt-4o-mini                | 1603.73 |
|   2 | mistral:pixtral-12b-2409          | 1568.49 |
|   1 | anthropic:claude-3-haiku-20240307 | 1524.71 |
|   0 | openai:gpt-4o                     | 1524.58 |
|   4 | mistral:pixtral-large-latest      | 1278.49 |

# Win rate table

|     | model                             | games_won | games_played | win_rate |
| --: | :-------------------------------- | --------: | -----------: | -------: |
|   0 | openai:gpt-4o-mini                |        41 |           48 | 0.854167 |
|   1 | mistral:pixtral-12b-2409          |        41 |           65 | 0.630769 |
|   3 | anthropic:claude-3-haiku-20240307 |        20 |           39 | 0.512821 |
|   4 | openai:gpt-4o                     |        23 |           76 | 0.302632 |
|   2 | mistral:pixtral-large-latest      |         0 |           22 |        0 |

# Results matrix

![result matrix](result_matrix.png)

| #   | Player 1                          | Player 2                          | Games Won | Games Played | Win Rate |
| --- | --------------------------------- | --------------------------------- | --------- | ------------ | -------- |
| 1   | openai:gpt-4o-mini                | mistral:pixtral-12b-2409          | 9         | 11           | 0.818182 |
| 2   | openai:gpt-4o-mini                | mistral:pixtral-large-latest      | 3         | 3            | 1.000000 |
| 3   | openai:gpt-4o-mini                | anthropic:claude-3-haiku-20240307 | 5         | 8            | 0.625000 |
| 4   | openai:gpt-4o-mini                | openai:gpt-4o                     | 24        | 26           | 0.923077 |
| 5   | mistral:pixtral-12b-2409          | openai:gpt-4o-mini                | 2         | 11           | 0.181818 |
| 6   | mistral:pixtral-12b-2409          | mistral:pixtral-large-latest      | 6         | 6            | 1.000000 |
| 7   | mistral:pixtral-12b-2409          | anthropic:claude-3-haiku-20240307 | 8         | 14           | 0.571429 |
| 8   | mistral:pixtral-12b-2409          | openai:gpt-4o                     | 25        | 34           | 0.735294 |
| 9   | mistral:pixtral-large-latest      | openai:gpt-4o-mini                | 0         | 3            | 0.000000 |
| 10  | mistral:pixtral-large-latest      | mistral:pixtral-12b-2409          | 0         | 6            | 0.000000 |
| 11  | mistral:pixtral-large-latest      | anthropic:claude-3-haiku-20240307 | 0         | 7            | 0.000000 |
| 12  | mistral:pixtral-large-latest      | openai:gpt-4o                     | 0         | 6            | 0.000000 |
| 13  | anthropic:claude-3-haiku-20240307 | openai:gpt-4o-mini                | 3         | 8            | 0.375000 |
| 14  | anthropic:claude-3-haiku-20240307 | mistral:pixtral-12b-2409          | 6         | 14           | 0.428571 |
| 15  | anthropic:claude-3-haiku-20240307 | mistral:pixtral-large-latest      | 7         | 7            | 1.000000 |
| 16  | anthropic:claude-3-haiku-20240307 | openai:gpt-4o                     | 4         | 10           | 0.400000 |
| 17  | openai:gpt-4o                     | openai:gpt-4o-mini                | 2         | 26           | 0.076923 |
| 18  | openai:gpt-4o                     | mistral:pixtral-12b-2409          | 9         | 34           | 0.264706 |
| 19  | openai:gpt-4o                     | mistral:pixtral-large-latest      | 6         | 6            | 1.000000 |
| 20  | openai:gpt-4o                     | anthropic:claude-3-haiku-20240307 | 6         | 10           | 0.600000 |
