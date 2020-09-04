class Board:
    def __init__(self):
        self.curr_board_state = [
            ['-', '-', '-'],
            ['-', '-', '-'],
            ['-', '-', '-']
        ]

        self.turn = 'X'

        self._ROWS = 3
        self._COLS = 3

    def draw_board(self):
        """
        Draws the board by looping over
        :return: nothing
        """
        for row in range(0, self._ROWS):
            for col in range(0, self._COLS):
                print(f'{self.curr_board_state[row][col]} | ', end="")
            print()

    def is_valid_move(self, x_cord, y_cord):
        """
        A method to check whether a given move is valid or not
        :param x_cord: x coordinate of the current move
        :param y_cord: y coordinate of the current move
        :return: whether the move is true or false
        """
        if x_cord < 0 or x_cord > 2 or y_cord < 0 or y_cord > 2:
            return False
        if self.curr_board_state[x_cord][y_cord] != '-':
            return False

        return True

    def has_ended(self):
        """
        A method that checks whether the game has ended or not
        :return: Checks if the game has ended and returns the winner at each of the case
        """

        # vertical win
        for col in range(0, self._COLS):
            if (self.curr_board_state[0][col] != '-' and
                    self.curr_board_state[0][col] == self.curr_board_state[1][col] and
                    self.curr_board_state[1][col] == self.curr_board_state[1][col]):
                return self.curr_board_state[0][col], True

        # horizontal win
        for row in range(0, self._ROWS):
            if (self.curr_board_state[row][0] != '-' and
                    self.curr_board_state[row][0] == self.curr_board_state[row][1] and
                    self.curr_board_state[row][1] == self.curr_board_state[row][2]):
                return self.curr_board_state[row][0], True

        # right diagonal win
        if (self.curr_board_state[0][0] != '-' and
                self.curr_board_state[0][0] == self.curr_board_state[1][1] and
                self.curr_board_state[1][1] == self.curr_board_state[2][2]):
            return self.curr_board_state[0][0], True

        # right diagonal win
        if (self.curr_board_state[2][0] != '-' and
                self.curr_board_state[2][0] == self.curr_board_state[1][1] and
                self.curr_board_state[1][1] == self.curr_board_state[0][2]):
            return self.curr_board_state[2][0], True

        # check to see if it is a draw
        # if there is an empty field in the board we can continue to play the game
        for row in range(0, self._ROWS):
            for col in range(0, self._COLS):
                if self.curr_board_state[row][col] == '-':
                    return '-', False

        # The game is a draw
        return '~', True

    def get_board(self):
        return self.curr_board_state
