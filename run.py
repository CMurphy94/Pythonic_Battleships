import random

BOARD_SIZE = 5
NUM_OF_SHIPS = 4

def board_setup():
    """
    Sets up to board size
    """
    board = []
    for i in range(BOARD_SIZE):
        row = ["0"] * BOARD_SIZE
        board.append(row)
    
    player_board = [['-' for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
    comp_board = [['-' for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]



def player_ships_setup():
    """
    Sets up the players ship locations
    """
    player_ships = []
    for i in range(NUM_OF_SHIPS):
        ship_row = random.randint(0, BOARD_SIZE-1)
        ship_col = random.randint(0, BOARD_SIZE-1)
        player_ships.append((ship_row, ship_col))
    print(f" player ships are located at the following locations: {player_ships}")



def computer_ships_setup():
    """
    Sets up the computers ship locations
    """
    comp_ships = []
    for i in range(NUM_OF_SHIPS):
        ship_row = random.randint(0, BOARD_SIZE-1)
        ship_col = random.randint(0, BOARD_SIZE-1)
        comp_ships.append((ship_row, ship_col))


def gameplay():
    """
    Runs the game
    """
    while True:
        x = int(input("Enter the column you'd like to guess: "))
        y = int(input("Enter the row you'd like to guess: "))

        if (x,y) in comp_ships:
            print("You Hit! Nice Job!")
            comp_board[x][y] = "X"
            comp_ships.remove((x, y))

        else:
            print("You missed!")
            comp_board[x][y] = "O"


def main():
    board_setup()
    player_ships_setup()
    computer_ships_setup()
    gameplay()

main()