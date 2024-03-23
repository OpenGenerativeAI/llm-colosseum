import diambra.arena
from diambra.arena import SpaceTypes, EnvironmentSettingsMultiAgent
from .robot import Robot


def main():
    # Environment Settings
    settings = EnvironmentSettingsMultiAgent()  # Multi Agents environment

    # --- Environment settings ---

    # If to use discrete or multi_discrete action space
    settings.action_space = (SpaceTypes.DISCRETE, SpaceTypes.DISCRETE)

    # --- Episode settings ---

    # Characters to be used, automatically extended with None for games
    # requiring to select more than one character (e.g. Tekken Tag Tournament)
    settings.characters = ("Ryu", "Ken")

    # Characters outfit
    settings.outfits = (2, 2)

    settings.frame_shape = (0, 0, 0)  # RBG with default size

    env = diambra.arena.make("sfiii3n", settings, render_mode="human")

    observation, info = env.reset(seed=42)

    robot_gpt = Robot(action_space=env.action_space[0])
    robot_mistral = Robot(action_space=env.action_space[1])

    robot_gpt.observe(observation)
    robot_mistral.observe(observation)

    while True:
        env.render()

        # Plan
        robot_gpt.plan()
        robot_mistral.plan()

        # Act
        actions = [robot_gpt.act(), robot_mistral.act()]

        print("Actions: {}".format(actions))
        # Execute actions in the game
        observation, reward, terminated, truncated, info = env.step(actions)

        done = terminated or truncated
        print("Reward: {}".format(reward))
        print("Done: {}".format(done))
        print("Info: {}".format(info))

        if done:
            # Optionally, change episode settings here
            options = {}
            options["characters"] = (None, None)
            options["char_outfits"] = (5, 5)
            observation, info = env.reset(options=options)
            break

        # Observe the environment
        robot_gpt.observe(observation)
        robot_mistral.observe(observation)

    env.close()

    # Return success
    return 0


if __name__ == "__main__":
    main()
