from __future__ import annotations


class GameResult:

    def __init__(self, winner, is_draw):
        self.winner = winner
        self.is_draw = is_draw

    @staticmethod
    def no_draw(winner) -> GameResult:
        return GameResult(winner, False)

    @staticmethod
    def draw() -> GameResult:
        return GameResult(None, True)

    def print(self) -> None:
        if self.is_draw:
            print('Draw!')
        else:
            print(f'{self.winner.name} wins!')
