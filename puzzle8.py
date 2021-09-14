"""
Write a class for the initial state. This will be the first input in the main function
Preferrably it will be a 3x3 matrix

The input matrix will be then
Find the

- Current config of tiles

8puzzle class:
    1-D array input for the puzzle
    function, shuffle: -fill the length 9 array with numbers 1 to 8, make sure one of them is empty " "
    for each move let's write a function
        down
        up
        left
        right
    function, ifgoalstate(THEgoalstate): compare the input array with the current state
    function, printboard: print the board as a 3x3 table



 """
import random
class Puzzle8:

    def __init__(self):
        self.board = board = [1,2,3,4,5,6,7,8," "]

    def shuffle(self):
        random.shuffle(self.board)

    def swap_tiles(self, target_tile, cur_tile):
        temp = self.board[target_tile]
        self.board[target_tile] = self.board[cur_tile]
        self.board[cur_tile] = temp

    def move_up(self, cur_tile):
        if self.board[cur_tile-3] < 0:
            if self.board[cur_tile-3] == " ":
                swap_tiles(cur_tile-3, cur_tile)

    def move_down(cur_tile):
        if self.board[cur_tile+3] > 9:
            if self.board[cur_tile+3] == " ":
                swap_tiles(cur_tile+3, cur_tile)

    def move_right(cur_tile):
        if self.board[cur_tile+1] > 9:
            if self.board[cur_tile+1] == " ":
                swap_tiles(cur_tile+1, cur_tile)

    def move_right(cur_tile):
        if self.board[cur_tile-1] < 0:
            if self.board[cur_tile-1] == " ":
                swap_tiles(cur_tile-1, cur_tile)





myPuzzle = Puzzle8()
myPuzzle.shuffle()
print(myPuzzle.board)


