from game_result import GameResult
from player import Player
from board import Board


class Game:

    def __init__(self):
        self.players = [
            Player(input('Enter first player\'s name: '), "X"),
            Player(input("Enter second player\'s name: "), "O")
        ]
        self.board = Board()

    def play(self) -> GameResult:
        self.board.print()
        for i in range(9):
            self.make_move(self.players[i % 2])
            self.board.print()
            if self.is_winner(self.players[i % 2]):
                return GameResult.no_draw(self.players[i % 2])
        return GameResult.draw()

    def make_move(self, player) -> None:
        print(f'{player}\'s turn.')
        row = self.get_row()
        column = self.get_column()
        if not self.board.is_empty_field(row - 1, column - 1):
            print('This field is already taken!')
            self.make_move(player)
            return
        self.board.board[row - 1][column - 1] = player.symbol

    def get_row(self) -> int:
        while True:
            (row, is_integer) = self.try_parse_to_int(input('Enter row: '))
            if not is_integer:
                print('Row must be an integer!')
                continue
            if row < 1 or row > 3:
                print('Row must be in range 1-3!')
                continue
            return row

    def get_column(self) -> int:
        while True:
            (column, is_integer) = self.try_parse_to_int(input('Enter column: '))
            if not is_integer:
                print('Column must be an integer!')
                continue
            if column < 1 or column > 3:
                print('Column must be in range 1-3!')
                continue
            return column

    def is_winner(self, player) -> bool:
        return self.is_horizontal_win_condition_meet(player.symbol) or \
            self.is_vertical_win_condition_meet(player.symbol) or \
            self.is_diagonal_win_condition_meet(player.symbol)

    def is_horizontal_win_condition_meet(self, symbol) -> bool:
        for row in self.board.board:
            if row[0] == row[1] == row[2] == symbol:
                return True
        return False

    def is_vertical_win_condition_meet(self, symbol) -> bool:
        for column in range(3):
            if self.board.board[0][column] == self.board.board[1][column] == self.board.board[2][column] == symbol:
                return True
        return False

    def is_diagonal_win_condition_meet(self, symbol) -> bool:
        return self.board.board[0][0] == self.board.board[1][1] == self.board.board[2][2] == symbol or \
            self.board.board[0][2] == self.board.board[1][1] == self.board.board[2][0] == symbol

    @staticmethod
    def try_parse_to_int(value) -> (int, bool):
        try:
            return int(value), True
        except ValueError:
            return value, False
