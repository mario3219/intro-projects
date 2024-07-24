class TicTacToeBoard:

    def __init__(self):
        self.board = [['-','-','-'],['-','-','-'],['-','-','-']]

    def get(self, row, col):
        return self.board[row][col]

    def is_empty(self, row, col):
        if self.board[row][col] == '-':
            return True
        else:
            return False

    def place(self, marker, row, col):
        if marker != 'O' and marker != 'X':
            return False
        if self.is_empty(row, col):
            self.board[row][col] = marker
            return True
        else:
            return False


    def is_full(self):
        for row in self.board:
            for col in row:
                if col == '-':
                    return False
        return True

    def is_winner(self, marker):
        idx = [0,1,2]
        count = 0

        # horizontal check
        for row in idx:
            for col in idx:
                if self.board[row][col] == marker:
                    count += 1
                else:
                    count = 0
                if count >= 3:
                    return True

        # vertical check        
        for col in idx:
            for row in idx:
                if self.board[row][col] == marker:
                    count += 1
                else:
                    count = 0
                if count >= 3:
                    return True
                
        # diagonal check        
        if self.board[0][0] == marker:
            if self.board[1][1] == marker:
                if self.board[2][2] == marker:
                    return True
        if self.board[0][2] == marker:
            if self.board[1][1] == marker:
                if self.board[2][0] == marker:
                    return True
        
        return False

    def restart(self):
        self.board = [['-','-','-'],['-','-','-'],['-','-','-']]

    def print_board(self):
        for row in self.board:
            print(row)
    
# -----------------------

if __name__ == '__main__':

    board = TicTacToeBoard()
    board.print_board()
    print(board.get(1,1))

    print(board.is_full())

    idx = [0, 1, 2]
    for row in idx:
        for col in idx:
            board.place('X', row, col)

    board.print_board()
    print(board.is_full())

    print("----test horizontal----")

    board.restart()
    for col in idx:
        board.place('X', 1, col)

    board.print_board()
    print(board.is_winner('X'))

    print("----test vertical----")

    board.restart()
    for row in idx:
        board.place('X', row, 1)

    board.print_board()
    print(board.is_winner('X'))

    print("----test diagonal----")

    board.restart()
    for row in idx:
        board.place('X', row, row)

    board.print_board()
    print(board.is_winner('X'))

    board.restart()
    for row in idx:
        board.place('X', 2-row, row)

    board.print_board()
    print(board.is_winner('X'))
