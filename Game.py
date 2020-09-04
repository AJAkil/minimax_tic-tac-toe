class Game:
    def __init__(self, ai, board_object):
        self.result = None
        self.ai = ai
        self.board_object = board_object
        self.turn = 'X'

    def print_win_message(self):
        if self.result == 'X':
            print('The winner is X!!')
        elif self.result == 'O':
            print('The winner is O!!')
        elif self.result == '~':
            print('The match is a tie!!')

    def play_game(self):
        while True:
            self.board_object.draw_board()
            self.result = self.board_object.has_ended()

            # Checking to see if anybody won or not!
            self.print_win_message()

