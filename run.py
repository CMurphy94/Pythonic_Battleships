import random

BOARD_SIZE = 5
NUM_OF_SHIPS = 4


def board_setup():
    """
    Sets up to board size
    """
    global player_board
    global comp_board
    
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
    print("--------------------------------")
    print("Welcome to Pythonic Battleships.")
    print("Sink before you're sank!")
    print("--------------------------------")
    print()
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


def computer_guess():
    """
    Ensures computer guesses a new location every round
    """
    global guessed_locations
    while True:
        comp_x = random.randint(0, BOARD_SIZE-1)
        comp_y = random.randint(0, BOARD_SIZE-1)
        if (comp_x, comp_y) not in guessed_locations:
            guessed_locations.append((comp_x, comp_y))
            break
    return comp_x, comp_y
        

def gameplay():
    """
    Runs the game
    """
    global guessed_locations
    guessed_locations = []
    player_guessed_locations = []
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
            x = input("Enter the row you'd like to guess: ")
            if not x.isdigit():
                raise ValueError("You need to input a number. For example 1 instead of One.")
            x = int(x)

            y = input("Enter the column you'd like to guess: ")
            if not y.isdigit():
                raise ValueError("You need to input a number. For example 1 instead of One.")
            y = int(y)

            if not (0 <= x < BOARD_SIZE) or not (0 <= y < BOARD_SIZE):
                raise ValueError("You need to enter a number that will be within the size of the board (0 - 4).")
            if (x, y) in player_guessed_locations:
                raise ValueError("You have already guessed this location. Please guess somewhere new, the ships don't move.")

            player_guessed_locations.append((x, y))

        except ValueError as e:
            print(e)
            continue

        except TypeError:
            print("You need input the number itself. For example 1 instead of One.")
            continue
        if (x, y) in comp_ships:
            print()
            print("You Hit! Nice Job!")
            comp_board[x][y] = "X"
            comp_ships.remove((x, y))
        else:
            print()
            print("You missed!")
            comp_board[x][y] = "O"

        if not comp_ships:
            print("--------------------------------------------------")
            print("You sank all the enemy ships! Nice job on winning!")
            print("--------------------------------------------------")
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
            print()
            print("You got Hit!")
            print()
            player_board[x][y] = "X"
            player_ships.remove((x, y))
        else:
            print()
            print("The computer Missed!")
            print()
            player_board[x][y] = "O"

        if not player_ships:
            print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
            print("All of your ships have been sunk! Game over!")
            print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
            break


def main():
    board_setup()
    player_ships_setup()
    computer_ships_setup()
    gameplay()


main()