import random

BOARD_SIZE = 5
NUM_OF_SHIPS = 4

def board_setup():
    global player_board
    global comp_board
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
    global player_ships
    player_ships = []
    ship_locations = set()
    while len(ship_locations) < NUM_OF_SHIPS:
        player_ship_row = random.randint(0, BOARD_SIZE-1)
        player_ship_col = random.randint(0, BOARD_SIZE-1)
        ship_locations.add((player_ship_row, player_ship_col))

    player_ships = list(ship_locations)
    for (x, y) in player_ships:
        player_board[x][y] = "S"
    print(f"Player ships are located at the following locations: {player_ships}")
    print()



def computer_ships_setup():
    """
    Sets up the computers ship locations
    """
    global comp_ships
    comp_ships = []
    ship_locations = set()
    while len(ship_locations) < NUM_OF_SHIPS:
        comp_ship_row = random.randint(0, BOARD_SIZE-1)
        comp_ship_col = random.randint(0, BOARD_SIZE-1)
        ship_locations.add((comp_ship_row, comp_ship_col))
    
    comp_ships = list(ship_locations)


def gameplay():
    """
    Runs the game
    """
    guessed_locations = []
    while True:
        print("Your board and ships: ")
        for row in player_board:
            print(" ".join(row))
        
        print()
        print("Computers board: ")
        for row in comp_board:
            print(" ".join(row))
        
        print()

        try:
            x = int(input("Enter the column you'd like to guess: "))
            y = int(input("Enter the row you'd like to guess: "))
            if not (0 <= x < BOARD_SIZE) or not (0 <= y < BOARD_SIZE):
                raise ValueError("You need to enter a number that will be within the size of the board (0 - 4).")
            if (x, y) in guessed_locations:
                raise ValueError("You have already guessed this location. Please guess somewhere new, the ships don't move.")

        except ValueError:
            print("You need to input a number. For example 1 instead of One.")
            continue

        guessed_locations.append((x, y))

        if (x,y) in comp_ships:
            print("You Hit! Nice Job!")
            comp_board[x][y] = "X"
            comp_ships.remove((x, y))

        else:
            print("You missed!")
            comp_board[x][y] = "O"

        if not comp_ships:
            print("You sank all the enemy ships! Nice job on winning!")
            break

        x = random.randint(0, BOARD_SIZE-1)
        y = random.randint(0, BOARD_SIZE-1)
        while (x, y) in guessed_locations:
            x = random.randint(0, BOARD_SIZE-1)
            y = random.randint(0, BOARD_SIZE-1)
        print()
        print(f"The computer is guessing that you have a ship at {x}, {y}")
        guessed_locations.append((x, y))

        if (x, y) in player_ships:
            print("You got Hit!")
            print()
            player_board[x][y] = "X"
            player_ships.remove((x, y))
        else:
            print("The computer Missed!")
            print()
            player_board[x][y] = "O"

        if not player_ships:
            print("All of your ships have been sunk! Game over!")
            break


def main():
    board_setup()
    player_ships_setup()
    computer_ships_setup()
    gameplay()

main()