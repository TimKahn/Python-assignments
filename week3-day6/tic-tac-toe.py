def main():
    game = TicTacToe()
    game.play_game()

class TicTacToe():
    def __init__(self):
        self.name = 'Tic-Tac-Toe Board'
        self.row1 = [(0,n) for n in range(0,3)]
        self.row2 = [(1,n) for n in range(0,3)]
        self.row3 = [(2,n) for n in range(0,3)]
        self.board = [self.row1, self.row2, self.row3]
        self.turn = 0
        self.player = 1
        self.input = ''
        self.status = 'playing'
        self.winner = 'nobody'

    def play_game(self):
        while self.status == 'playing':
            self.take_turn()
            self.update_board()
            self.update_status()
        print(self.status)
        self.display_board()

    def take_turn(self):
        self.turn += 1
        self.display_board()
        self.player = 2 - self.turn%2
        if self.player == 1:
            self.input = raw_input('Player X, where will you play? ') + ',X'
        else:
            self.input = raw_input('Player O, where will you play? ') + ',O'
        self.input = tuple(self.input.split(','))

    def display_board(self):
        for row in self.board: print(row)
        print('')

    def update_board(self):
        row = int(self.input[0])
        column = int(self.input[1])
        self.board[row][column] = self.input[2]

    def update_status(self):
        if self.turn >= 5 and any([self.check_rows(), self.check_columns()]):
            self.status = '\nPlayer ' + self.winner + ' wins!\n'
        elif self.turn == 9:
            self.status = 'Tie game!'
        else:
            return

    def check_rows(self):
        for row in self.board:
            if row[0] == row[1] == row[2]:
                self.winner = row[0]
                return True

    def check_columns(self):
        for j in range(3):
            column = [self.board[i][j] for i in range(3)]
            if column[0] == column[1] == column[2]:
                self.winner = column[0]
                return True

if __name__ == '__main__':
    main()
