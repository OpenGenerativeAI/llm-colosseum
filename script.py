from eval.game import Game


def main():
    # Environment Settings
    # Environment Settings

    game = Game(
        render=True,
        splash_screen=True,
        characters=["Ken", "Ken"],
        outfits=[1, 3],
        seed=42,
    )

    game.run()


if __name__ == "__main__":
    main()
