import os


class Board:
    size = 3

    def __init__(self):
        self.board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

    def is_empty_field(self, row, column) -> bool:
        return self.board[row][column] == " "

    def print(self) -> None:
        self.cls()
        print("   1   2   3   ")
        for row in range(Board.size):
            print(f'{row+1}', end=" ")
            for column in self.board[row]:
                print(f'[{column}]', end=" ")
            print()

    @staticmethod
    def cls() -> None:
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')