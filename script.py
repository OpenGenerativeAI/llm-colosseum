#!/usr/bin/env python3
import diambra.arena
from diambra.arena import SpaceTypes, EnvironmentSettingsMultiAgent


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

    while True:
        env.render()

        actions = env.action_space.sample()
        print("Actions: {}".format(actions))

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

    env.close()

    # Return success
    return 0


if __name__ == "__main__":
    main()
