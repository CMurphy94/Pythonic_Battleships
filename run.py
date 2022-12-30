import random

BOARD_SIZE = 5
NUM_OF_SHIPS = 4

def board_setup():
    board = []
    for i in range(BOARD_SIZE):
        row = ["0"] * BOARD_SIZE
        board.append(row)



def player_ships_setup():
    player_ships = []
    for i in range(NUM_OF_SHIPS):
        ship_row = random.randint(0, BOARD_SIZE-1)
        ship_col = random.randint(0, BOARD_SIZE-1)
        player_ships.append((ship_row, ship_col))
    
    print(f" player ships are located at the following locations: {player_ships}")


def computer_ships_setup():
    comp_ships = []
    for i in range(NUM_OF_SHIPS):
        ship_row = random.randint(0, BOARD_SIZE-1)
        ship_col = random.randint(0, BOARD_SIZE-1)
        comp_ships.append((ship_row, ship_col))

player_ships_setup()