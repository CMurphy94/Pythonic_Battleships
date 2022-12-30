BOARD_SIZE = 5
NUM_OF_SHIPS = 4

def board_setup():
    board = []
    for i in range(BOARD_SIZE):
        row = ["0"] * 5
        board.append(row)