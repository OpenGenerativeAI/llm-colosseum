import diambra.arena
from diambra.arena import SpaceTypes, EnvironmentSettingsMultiAgent
from agent import Robot, KEN_RED, KEN_GREEN


def main():
    # Environment Settings
    settings = EnvironmentSettingsMultiAgent()  # Multi Agents environment

    # --- Environment settings ---

    # If to use discrete or multi_discrete action space
    settings.action_space = (SpaceTypes.DISCRETE, SpaceTypes.DISCRETE)

    # --- Episode settings ---

    # Characters to be used, automatically extended with None for games
    # requiring to select more than one character (e.g. Tekken Tag Tournament)
    settings.characters = ("Ken", "Ken")
    settings.outfits = (1, 3)

    # Characters outfit

    settings.frame_shape = (0, 0, 0)  # RBG with default size

    env = diambra.arena.make("sfiii3n", settings, render_mode="human")

    observation, info = env.reset(seed=42)

    # Intiialize the robots
    robot_mistral = Robot(
        action_space=env.action_space["agent_0"],
        character="Ken",
        side=0,
        character_color=KEN_RED,
        ennemy_color=KEN_GREEN,
    )
    robot_gpt = Robot(
        action_space=env.action_space["agent_1"],
        character="Ryu",
        side=1,
        character_color=KEN_GREEN,
        ennemy_color=KEN_RED,
    )

    robot_mistral.observe(observation)
    robot_gpt.observe(observation)

    while True:
        env.render()

        # Plan
        robot_mistral.plan()
        robot_gpt.plan()

        # Act
        actions = {"agent_0": robot_mistral.act(), "agent_1": robot_gpt.act()}

        print("Actions: {}".format(actions))
        # Execute actions in the game
        observation, reward, terminated, truncated, info = env.step(actions)

        done = terminated or truncated
        # print("Reward: {}".format(reward))
        # print("Done: {}".format(done))
        # print("Info: {}".format(info))
        print(f"Observation: {observation}")

        if done:
            # Optionally, change episode settings here
            options = {}
            options["characters"] = (None, None)
            options["char_outfits"] = (5, 5)
            observation, info = env.reset(options=options)
            break

        # Observe the environment
        robot_mistral.observe(observation)
        robot_gpt.observe(observation)

    env.close()

    # Return success
    return 0


if __name__ == "__main__":
    main()
