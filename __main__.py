from game import Game


def main() -> None:
    game = Game()
    game_result = game.play()
    game_result.print()


if __name__ == '__main__':
    main()
