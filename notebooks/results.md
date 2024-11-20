# Elo Score

| Rank | Model                                                              |  Rating |
| ---: | :----------------------------------------------------------------- | ------: |
|    1 | openai:gpt-4o:text                                                 |  1912.5 |
|    2 | **openai:gpt-4o-mini:vision**                                      | 1835.27 |
|    3 | openai:gpt-4o-mini:text                                            | 1670.89 |
|    4 | **openai:gpt-4o:vision**                                           | 1656.93 |
|    5 | **mistral:pixtral-large-latest:vision**                            | 1654.61 |
|    6 | **mistral:pixtral-12b-2409:vision**                                | 1590.77 |
|    7 | mistral:pixtral-12b-2409:text                                      | 1569.03 |
|    8 | together:meta-llama/Llama-3.2-90B-Vision-Instruct-Turbo:text       | 1441.45 |
|    9 | **anthropic:claude-3-haiku-20240307:vision**                       | 1364.87 |
|   10 | mistral:pixtral-large-latest:text                                  | 1356.32 |
|   11 | anthropic:claude-3-haiku-20240307:text                             |  1333.6 |
|   12 | **anthropic:claude-3-sonnet-20240229:vision**                      | 1314.61 |
|   13 | **together:meta-llama/Llama-3.2-90B-Vision-Instruct-Turbo:vision** | 1269.84 |
|   14 | anthropic:claude-3-sonnet-20240229:text                            | 1029.31 |

# Results matrix

![result matrix](result_matrix.png)

|     | model_1                                                        | model_2                                                        | games_won | games_played |  win_rate |
| --: | :------------------------------------------------------------- | :------------------------------------------------------------- | --------: | -----------: | --------: |
|   3 | together:meta-llama/Llama-3.2-90B-Vision-Instruct-Turbo:text   | mistral:pixtral-large-latest:text                              |         1 |            2 |       0.5 |
|   8 | together:meta-llama/Llama-3.2-90B-Vision-Instruct-Turbo:text   | anthropic:claude-3-sonnet-20240229:text                        |         7 |            7 |         1 |
|  16 | together:meta-llama/Llama-3.2-90B-Vision-Instruct-Turbo:vision | anthropic:claude-3-sonnet-20240229:vision                      |         0 |            5 |         0 |
|  17 | together:meta-llama/Llama-3.2-90B-Vision-Instruct-Turbo:vision | mistral:pixtral-large-latest:text                              |         2 |            7 |  0.285714 |
|  18 | together:meta-llama/Llama-3.2-90B-Vision-Instruct-Turbo:vision | openai:gpt-4o-mini:vision                                      |         0 |            3 |         0 |
|  19 | together:meta-llama/Llama-3.2-90B-Vision-Instruct-Turbo:vision | mistral:pixtral-large-latest:vision                            |         0 |            4 |         0 |
|  20 | together:meta-llama/Llama-3.2-90B-Vision-Instruct-Turbo:vision | anthropic:claude-3-haiku-20240307:vision                       |         0 |            3 |         0 |
|  21 | together:meta-llama/Llama-3.2-90B-Vision-Instruct-Turbo:vision | anthropic:claude-3-haiku-20240307:text                         |         0 |            5 |         0 |
|  22 | together:meta-llama/Llama-3.2-90B-Vision-Instruct-Turbo:vision | anthropic:claude-3-sonnet-20240229:text                        |         6 |           13 |  0.461538 |
|  23 | together:meta-llama/Llama-3.2-90B-Vision-Instruct-Turbo:vision | openai:gpt-4o:vision                                           |         0 |            5 |         0 |
|  24 | together:meta-llama/Llama-3.2-90B-Vision-Instruct-Turbo:vision | mistral:pixtral-12b-2409:text                                  |         0 |            4 |         0 |
|  25 | together:meta-llama/Llama-3.2-90B-Vision-Instruct-Turbo:vision | openai:gpt-4o-mini:text                                        |         0 |            4 |         0 |
|  26 | together:meta-llama/Llama-3.2-90B-Vision-Instruct-Turbo:vision | openai:gpt-4o:text                                             |         0 |            3 |         0 |
|  27 | together:meta-llama/Llama-3.2-90B-Vision-Instruct-Turbo:vision | mistral:pixtral-12b-2409:vision                                |         0 |            5 |         0 |
|  29 | anthropic:claude-3-sonnet-20240229:vision                      | together:meta-llama/Llama-3.2-90B-Vision-Instruct-Turbo:vision |         5 |            5 |         1 |
|  31 | anthropic:claude-3-sonnet-20240229:vision                      | mistral:pixtral-large-latest:text                              |         1 |            7 |  0.142857 |
|  32 | anthropic:claude-3-sonnet-20240229:vision                      | openai:gpt-4o-mini:vision                                      |         0 |            3 |         0 |
|  33 | anthropic:claude-3-sonnet-20240229:vision                      | mistral:pixtral-large-latest:vision                            |         0 |            5 |         0 |
|  34 | anthropic:claude-3-sonnet-20240229:vision                      | anthropic:claude-3-haiku-20240307:vision                       |         5 |            6 |  0.833333 |
|  35 | anthropic:claude-3-sonnet-20240229:vision                      | anthropic:claude-3-haiku-20240307:text                         |         4 |            6 |  0.666667 |
|  36 | anthropic:claude-3-sonnet-20240229:vision                      | anthropic:claude-3-sonnet-20240229:text                        |         8 |            9 |  0.888889 |
|  37 | anthropic:claude-3-sonnet-20240229:vision                      | openai:gpt-4o:vision                                           |         0 |            2 |         0 |
|  38 | anthropic:claude-3-sonnet-20240229:vision                      | mistral:pixtral-12b-2409:text                                  |         0 |            3 |         0 |
|  39 | anthropic:claude-3-sonnet-20240229:vision                      | openai:gpt-4o-mini:text                                        |         0 |            6 |         0 |
|  40 | anthropic:claude-3-sonnet-20240229:vision                      | openai:gpt-4o:text                                             |         0 |            2 |         0 |
|  41 | anthropic:claude-3-sonnet-20240229:vision                      | mistral:pixtral-12b-2409:vision                                |         0 |            4 |         0 |
|  42 | mistral:pixtral-large-latest:text                              | together:meta-llama/Llama-3.2-90B-Vision-Instruct-Turbo:text   |         1 |            2 |       0.5 |
|  43 | mistral:pixtral-large-latest:text                              | together:meta-llama/Llama-3.2-90B-Vision-Instruct-Turbo:vision |         5 |            7 |  0.714286 |
|  44 | mistral:pixtral-large-latest:text                              | anthropic:claude-3-sonnet-20240229:vision                      |         6 |            7 |  0.857143 |
|  46 | mistral:pixtral-large-latest:text                              | openai:gpt-4o-mini:vision                                      |         0 |            7 |         0 |
|  47 | mistral:pixtral-large-latest:text                              | mistral:pixtral-large-latest:vision                            |         0 |            7 |         0 |
|  48 | mistral:pixtral-large-latest:text                              | anthropic:claude-3-haiku-20240307:vision                       |         0 |            2 |         0 |
|  49 | mistral:pixtral-large-latest:text                              | anthropic:claude-3-haiku-20240307:text                         |         0 |            4 |         0 |
|  50 | mistral:pixtral-large-latest:text                              | anthropic:claude-3-sonnet-20240229:text                        |        13 |           14 |  0.928571 |
|  51 | mistral:pixtral-large-latest:text                              | openai:gpt-4o:vision                                           |         0 |            3 |         0 |
|  52 | mistral:pixtral-large-latest:text                              | mistral:pixtral-12b-2409:text                                  |         0 |            3 |         0 |
|  53 | mistral:pixtral-large-latest:text                              | openai:gpt-4o-mini:text                                        |         0 |            7 |         0 |
|  54 | mistral:pixtral-large-latest:text                              | openai:gpt-4o:text                                             |         0 |            4 |         0 |
|  55 | mistral:pixtral-large-latest:text                              | mistral:pixtral-12b-2409:vision                                |         0 |            3 |         0 |
|  57 | openai:gpt-4o-mini:vision                                      | together:meta-llama/Llama-3.2-90B-Vision-Instruct-Turbo:vision |         3 |            3 |         1 |
|  58 | openai:gpt-4o-mini:vision                                      | anthropic:claude-3-sonnet-20240229:vision                      |         3 |            3 |         1 |
|  59 | openai:gpt-4o-mini:vision                                      | mistral:pixtral-large-latest:text                              |         7 |            7 |         1 |
|  61 | openai:gpt-4o-mini:vision                                      | mistral:pixtral-large-latest:vision                            |         5 |            5 |         1 |
|  62 | openai:gpt-4o-mini:vision                                      | anthropic:claude-3-haiku-20240307:vision                       |         5 |            5 |         1 |
|  63 | openai:gpt-4o-mini:vision                                      | anthropic:claude-3-haiku-20240307:text                         |         4 |            4 |         1 |
|  64 | openai:gpt-4o-mini:vision                                      | anthropic:claude-3-sonnet-20240229:text                        |         5 |            5 |         1 |
|  65 | openai:gpt-4o-mini:vision                                      | openai:gpt-4o:vision                                           |        12 |           12 |         1 |
|  66 | openai:gpt-4o-mini:vision                                      | mistral:pixtral-12b-2409:text                                  |         5 |            5 |         1 |
|  67 | openai:gpt-4o-mini:vision                                      | openai:gpt-4o-mini:text                                        |         4 |            4 |         1 |
|  68 | openai:gpt-4o-mini:vision                                      | openai:gpt-4o:text                                             |         0 |            4 |         0 |
|  69 | openai:gpt-4o-mini:vision                                      | mistral:pixtral-12b-2409:vision                                |         5 |            5 |         1 |
|  71 | mistral:pixtral-large-latest:vision                            | together:meta-llama/Llama-3.2-90B-Vision-Instruct-Turbo:vision |         4 |            4 |         1 |
|  72 | mistral:pixtral-large-latest:vision                            | anthropic:claude-3-sonnet-20240229:vision                      |         5 |            5 |         1 |
|  73 | mistral:pixtral-large-latest:vision                            | mistral:pixtral-large-latest:text                              |         7 |            7 |         1 |
|  74 | mistral:pixtral-large-latest:vision                            | openai:gpt-4o-mini:vision                                      |         0 |            5 |         0 |
|  76 | mistral:pixtral-large-latest:vision                            | anthropic:claude-3-haiku-20240307:vision                       |         9 |           10 |       0.9 |
|  77 | mistral:pixtral-large-latest:vision                            | anthropic:claude-3-haiku-20240307:text                         |         2 |            3 |  0.666667 |
|  78 | mistral:pixtral-large-latest:vision                            | anthropic:claude-3-sonnet-20240229:text                        |         9 |            9 |         1 |
|  79 | mistral:pixtral-large-latest:vision                            | openai:gpt-4o:vision                                           |         0 |            6 |         0 |
|  80 | mistral:pixtral-large-latest:vision                            | mistral:pixtral-12b-2409:text                                  |         3 |            4 |      0.75 |
|  81 | mistral:pixtral-large-latest:vision                            | openai:gpt-4o-mini:text                                        |         0 |            4 |         0 |
|  82 | mistral:pixtral-large-latest:vision                            | openai:gpt-4o:text                                             |         0 |            6 |         0 |
|  83 | mistral:pixtral-large-latest:vision                            | mistral:pixtral-12b-2409:vision                                |         6 |            7 |  0.857143 |
|  85 | anthropic:claude-3-haiku-20240307:vision                       | together:meta-llama/Llama-3.2-90B-Vision-Instruct-Turbo:vision |         3 |            3 |         1 |
|  86 | anthropic:claude-3-haiku-20240307:vision                       | anthropic:claude-3-sonnet-20240229:vision                      |         1 |            6 |  0.166667 |
|  87 | anthropic:claude-3-haiku-20240307:vision                       | mistral:pixtral-large-latest:text                              |         2 |            2 |         1 |
|  88 | anthropic:claude-3-haiku-20240307:vision                       | openai:gpt-4o-mini:vision                                      |         0 |            5 |         0 |
|  89 | anthropic:claude-3-haiku-20240307:vision                       | mistral:pixtral-large-latest:vision                            |         1 |           10 |       0.1 |
|  91 | anthropic:claude-3-haiku-20240307:vision                       | anthropic:claude-3-haiku-20240307:text                         |         8 |            8 |         1 |
|  92 | anthropic:claude-3-haiku-20240307:vision                       | anthropic:claude-3-sonnet-20240229:text                        |         5 |            7 |  0.714286 |
|  93 | anthropic:claude-3-haiku-20240307:vision                       | openai:gpt-4o:vision                                           |         4 |           10 |       0.4 |
|  94 | anthropic:claude-3-haiku-20240307:vision                       | mistral:pixtral-12b-2409:text                                  |         6 |           14 |  0.428571 |
|  95 | anthropic:claude-3-haiku-20240307:vision                       | openai:gpt-4o-mini:text                                        |         3 |            8 |     0.375 |
|  96 | anthropic:claude-3-haiku-20240307:vision                       | openai:gpt-4o:text                                             |         0 |            6 |         0 |
|  97 | anthropic:claude-3-haiku-20240307:vision                       | mistral:pixtral-12b-2409:vision                                |         0 |            6 |         0 |
|  99 | anthropic:claude-3-haiku-20240307:text                         | together:meta-llama/Llama-3.2-90B-Vision-Instruct-Turbo:vision |         5 |            5 |         1 |
| 100 | anthropic:claude-3-haiku-20240307:text                         | anthropic:claude-3-sonnet-20240229:vision                      |         2 |            6 |  0.333333 |
| 101 | anthropic:claude-3-haiku-20240307:text                         | mistral:pixtral-large-latest:text                              |         4 |            4 |         1 |
| 102 | anthropic:claude-3-haiku-20240307:text                         | openai:gpt-4o-mini:vision                                      |         0 |            4 |         0 |
| 103 | anthropic:claude-3-haiku-20240307:text                         | mistral:pixtral-large-latest:vision                            |         1 |            3 |  0.333333 |
| 104 | anthropic:claude-3-haiku-20240307:text                         | anthropic:claude-3-haiku-20240307:vision                       |         0 |            8 |         0 |
| 106 | anthropic:claude-3-haiku-20240307:text                         | anthropic:claude-3-sonnet-20240229:text                        |         6 |           11 |  0.545455 |
| 107 | anthropic:claude-3-haiku-20240307:text                         | openai:gpt-4o:vision                                           |         0 |            4 |         0 |
| 108 | anthropic:claude-3-haiku-20240307:text                         | mistral:pixtral-12b-2409:text                                  |         0 |            4 |         0 |
| 109 | anthropic:claude-3-haiku-20240307:text                         | openai:gpt-4o-mini:text                                        |         0 |            3 |         0 |
| 110 | anthropic:claude-3-haiku-20240307:text                         | openai:gpt-4o:text                                             |         0 |            6 |         0 |
| 111 | anthropic:claude-3-haiku-20240307:text                         | mistral:pixtral-12b-2409:vision                                |         0 |            3 |         0 |
| 112 | anthropic:claude-3-sonnet-20240229:text                        | together:meta-llama/Llama-3.2-90B-Vision-Instruct-Turbo:text   |         0 |            7 |         0 |
| 113 | anthropic:claude-3-sonnet-20240229:text                        | together:meta-llama/Llama-3.2-90B-Vision-Instruct-Turbo:vision |         7 |           13 |  0.538462 |
| 114 | anthropic:claude-3-sonnet-20240229:text                        | anthropic:claude-3-sonnet-20240229:vision                      |         1 |            9 |  0.111111 |
| 115 | anthropic:claude-3-sonnet-20240229:text                        | mistral:pixtral-large-latest:text                              |         1 |           14 | 0.0714286 |
| 116 | anthropic:claude-3-sonnet-20240229:text                        | openai:gpt-4o-mini:vision                                      |         0 |            5 |         0 |
| 117 | anthropic:claude-3-sonnet-20240229:text                        | mistral:pixtral-large-latest:vision                            |         0 |            9 |         0 |
| 118 | anthropic:claude-3-sonnet-20240229:text                        | anthropic:claude-3-haiku-20240307:vision                       |         2 |            7 |  0.285714 |
| 119 | anthropic:claude-3-sonnet-20240229:text                        | anthropic:claude-3-haiku-20240307:text                         |         5 |           11 |  0.454545 |
| 121 | anthropic:claude-3-sonnet-20240229:text                        | openai:gpt-4o:vision                                           |         0 |            5 |         0 |
| 122 | anthropic:claude-3-sonnet-20240229:text                        | mistral:pixtral-12b-2409:text                                  |         0 |           10 |         0 |
| 123 | anthropic:claude-3-sonnet-20240229:text                        | openai:gpt-4o-mini:text                                        |         0 |            7 |         0 |
| 124 | anthropic:claude-3-sonnet-20240229:text                        | openai:gpt-4o:text                                             |         0 |           11 |         0 |
| 125 | anthropic:claude-3-sonnet-20240229:text                        | mistral:pixtral-12b-2409:vision                                |         0 |           12 |         0 |
| 127 | openai:gpt-4o:vision                                           | together:meta-llama/Llama-3.2-90B-Vision-Instruct-Turbo:vision |         5 |            5 |         1 |
| 128 | openai:gpt-4o:vision                                           | anthropic:claude-3-sonnet-20240229:vision                      |         2 |            2 |         1 |
| 129 | openai:gpt-4o:vision                                           | mistral:pixtral-large-latest:text                              |         3 |            3 |         1 |
| 130 | openai:gpt-4o:vision                                           | openai:gpt-4o-mini:vision                                      |         0 |           12 |         0 |
| 131 | openai:gpt-4o:vision                                           | mistral:pixtral-large-latest:vision                            |         6 |            6 |         1 |
| 132 | openai:gpt-4o:vision                                           | anthropic:claude-3-haiku-20240307:vision                       |         6 |           10 |       0.6 |
| 133 | openai:gpt-4o:vision                                           | anthropic:claude-3-haiku-20240307:text                         |         4 |            4 |         1 |
| 134 | openai:gpt-4o:vision                                           | anthropic:claude-3-sonnet-20240229:text                        |         5 |            5 |         1 |
| 136 | openai:gpt-4o:vision                                           | mistral:pixtral-12b-2409:text                                  |         9 |           25 |      0.36 |
| 137 | openai:gpt-4o:vision                                           | openai:gpt-4o-mini:text                                        |         2 |           14 |  0.142857 |
| 138 | openai:gpt-4o:vision                                           | openai:gpt-4o:text                                             |         0 |           12 |         0 |
| 139 | openai:gpt-4o:vision                                           | mistral:pixtral-12b-2409:vision                                |         0 |            9 |         0 |
| 141 | mistral:pixtral-12b-2409:text                                  | together:meta-llama/Llama-3.2-90B-Vision-Instruct-Turbo:vision |         4 |            4 |         1 |
| 142 | mistral:pixtral-12b-2409:text                                  | anthropic:claude-3-sonnet-20240229:vision                      |         3 |            3 |         1 |
| 143 | mistral:pixtral-12b-2409:text                                  | mistral:pixtral-large-latest:text                              |         3 |            3 |         1 |
| 144 | mistral:pixtral-12b-2409:text                                  | openai:gpt-4o-mini:vision                                      |         0 |            5 |         0 |
| 145 | mistral:pixtral-12b-2409:text                                  | mistral:pixtral-large-latest:vision                            |         1 |            4 |      0.25 |
| 146 | mistral:pixtral-12b-2409:text                                  | anthropic:claude-3-haiku-20240307:vision                       |         8 |           14 |  0.571429 |
| 147 | mistral:pixtral-12b-2409:text                                  | anthropic:claude-3-haiku-20240307:text                         |         4 |            4 |         1 |
| 148 | mistral:pixtral-12b-2409:text                                  | anthropic:claude-3-sonnet-20240229:text                        |        10 |           10 |         1 |
| 149 | mistral:pixtral-12b-2409:text                                  | openai:gpt-4o:vision                                           |        16 |           25 |      0.64 |
| 151 | mistral:pixtral-12b-2409:text                                  | openai:gpt-4o-mini:text                                        |         2 |           11 |  0.181818 |
| 152 | mistral:pixtral-12b-2409:text                                  | openai:gpt-4o:text                                             |         0 |            5 |         0 |
| 153 | mistral:pixtral-12b-2409:text                                  | mistral:pixtral-12b-2409:vision                                |         0 |            2 |         0 |
| 155 | openai:gpt-4o-mini:text                                        | together:meta-llama/Llama-3.2-90B-Vision-Instruct-Turbo:vision |         4 |            4 |         1 |
| 156 | openai:gpt-4o-mini:text                                        | anthropic:claude-3-sonnet-20240229:vision                      |         6 |            6 |         1 |
| 157 | openai:gpt-4o-mini:text                                        | mistral:pixtral-large-latest:text                              |         7 |            7 |         1 |
| 158 | openai:gpt-4o-mini:text                                        | openai:gpt-4o-mini:vision                                      |         0 |            4 |         0 |
| 159 | openai:gpt-4o-mini:text                                        | mistral:pixtral-large-latest:vision                            |         4 |            4 |         1 |
| 160 | openai:gpt-4o-mini:text                                        | anthropic:claude-3-haiku-20240307:vision                       |         5 |            8 |     0.625 |
| 161 | openai:gpt-4o-mini:text                                        | anthropic:claude-3-haiku-20240307:text                         |         3 |            3 |         1 |
| 162 | openai:gpt-4o-mini:text                                        | anthropic:claude-3-sonnet-20240229:text                        |         7 |            7 |         1 |
| 163 | openai:gpt-4o-mini:text                                        | openai:gpt-4o:vision                                           |        12 |           14 |  0.857143 |
| 164 | openai:gpt-4o-mini:text                                        | mistral:pixtral-12b-2409:text                                  |         9 |           11 |  0.818182 |
| 166 | openai:gpt-4o-mini:text                                        | openai:gpt-4o:text                                             |         0 |            7 |         0 |
| 167 | openai:gpt-4o-mini:text                                        | mistral:pixtral-12b-2409:vision                                |         2 |            2 |         1 |
| 169 | openai:gpt-4o:text                                             | together:meta-llama/Llama-3.2-90B-Vision-Instruct-Turbo:vision |         3 |            3 |         1 |
| 170 | openai:gpt-4o:text                                             | anthropic:claude-3-sonnet-20240229:vision                      |         2 |            2 |         1 |
| 171 | openai:gpt-4o:text                                             | mistral:pixtral-large-latest:text                              |         4 |            4 |         1 |
| 172 | openai:gpt-4o:text                                             | openai:gpt-4o-mini:vision                                      |         4 |            4 |         1 |
| 173 | openai:gpt-4o:text                                             | mistral:pixtral-large-latest:vision                            |         6 |            6 |         1 |
| 174 | openai:gpt-4o:text                                             | anthropic:claude-3-haiku-20240307:vision                       |         6 |            6 |         1 |
| 175 | openai:gpt-4o:text                                             | anthropic:claude-3-haiku-20240307:text                         |         6 |            6 |         1 |
| 176 | openai:gpt-4o:text                                             | anthropic:claude-3-sonnet-20240229:text                        |        11 |           11 |         1 |
| 177 | openai:gpt-4o:text                                             | openai:gpt-4o:vision                                           |        12 |           12 |         1 |
| 178 | openai:gpt-4o:text                                             | mistral:pixtral-12b-2409:text                                  |         5 |            5 |         1 |
| 179 | openai:gpt-4o:text                                             | openai:gpt-4o-mini:text                                        |         7 |            7 |         1 |
| 181 | openai:gpt-4o:text                                             | mistral:pixtral-12b-2409:vision                                |         4 |            4 |         1 |
| 183 | mistral:pixtral-12b-2409:vision                                | together:meta-llama/Llama-3.2-90B-Vision-Instruct-Turbo:vision |         5 |            5 |         1 |
| 184 | mistral:pixtral-12b-2409:vision                                | anthropic:claude-3-sonnet-20240229:vision                      |         4 |            4 |         1 |
| 185 | mistral:pixtral-12b-2409:vision                                | mistral:pixtral-large-latest:text                              |         3 |            3 |         1 |
| 186 | mistral:pixtral-12b-2409:vision                                | openai:gpt-4o-mini:vision                                      |         0 |            5 |         0 |
| 187 | mistral:pixtral-12b-2409:vision                                | mistral:pixtral-large-latest:vision                            |         1 |            7 |  0.142857 |
| 188 | mistral:pixtral-12b-2409:vision                                | anthropic:claude-3-haiku-20240307:vision                       |         6 |            6 |         1 |
| 189 | mistral:pixtral-12b-2409:vision                                | anthropic:claude-3-haiku-20240307:text                         |         3 |            3 |         1 |
| 190 | mistral:pixtral-12b-2409:vision                                | anthropic:claude-3-sonnet-20240229:text                        |        12 |           12 |         1 |
| 191 | mistral:pixtral-12b-2409:vision                                | openai:gpt-4o:vision                                           |         9 |            9 |         1 |
| 192 | mistral:pixtral-12b-2409:vision                                | mistral:pixtral-12b-2409:text                                  |         2 |            2 |         1 |
| 193 | mistral:pixtral-12b-2409:vision                                | openai:gpt-4o-mini:text                                        |         0 |            2 |         0 |
| 194 | mistral:pixtral-12b-2409:vision                                | openai:gpt-4o:text                                             |         0 |            4 |         0 |
|   5 | 1                                                              |
