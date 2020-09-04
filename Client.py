from Board import Board


def main():
    g = Board()
    g.draw_board()
    turn, state_of_compl = g.has_ended()
    print(turn, state_of_compl)


if __name__ == '__main__':
    main()
