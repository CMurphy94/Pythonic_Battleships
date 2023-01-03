# Pythonic Battleships!

Pythonic Battleships is a simple easy to play Battleships game that is built within Python.
That game is set up on a 5x5 battlefield grid with both player and computer having 4 Battleships randomly deployed to the field.
The players goal is to find the location of and sink the computers Battleships, before the computer guesses the players.

## How to Play

As stated above the goal of this game is to sink the opponents Battleships. When the game starts you will be presented with two
grids. Titled the players board and computers board accordingly. You will notice a difference in these two boards in that
the player board will have four "S" numbers placed in random locations. This indentifies the location of the players ships.
Don't worry though the computer does not know the location of these. The player will then be asked to guess a row and column, if
they get it correct that section of the board will update to an "X" to indicate a hit and the player will be informed they've
sank a battleship. If the player misses they will also be informed of said miss, however the location guessed will update to a
"O" instead of a "X" to indicate the miss. Once the player makes a guess the computer will then make a guess back at the players
board. This will also be updated to show the player where the computer has guessed.

## Features

- Random ship generation and placement.
  - Four ships will always be placed for both the player and computer. No one space can occupy two ships.
- Play against the computer which makes guesses back against the player.
- Accepts the location of wherever the user wants to guess.
- Validation prevents the computer from guessing the same location twice.
- Validation also prevents the user from inputting anything other than a valid integer or from guessing the same location twice.
