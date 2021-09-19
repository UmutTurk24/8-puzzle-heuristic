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

class PriorityQueue(object):
    def __init__(self):
        self.queue = []

    def __str__(self):
        return ' '.join([str(i) for i in self.queue])

    # for checking if the queue is empty
    def isEmpty(self):
        return len(self.queue) == 0

    # for inserting an element in the queue
    def insert(self, data):
        self.queue.append(data)

    # for popping an element based on Priority
    def delete(self):
        try:
            max = 0
            for i in range(len(self.queue)):
                if self.queue[i] > self.queue[max]:
                    max = i
            item = self.queue[max]
            del self.queue[max]
            return item
        except IndexError:
            print()
            exit()

class Puzzle8:

    def __init__(self):
        self.board = board = [-1,1,2,3,4,5,6,7,8]

    def shuffle(self):
        random.shuffle(self.board)
        return self.board

    def swap_tiles(self, target_tile, cur_tile):
        temp = self.board[target_tile]
        self.board[target_tile] = self.board[cur_tile]
        self.board[cur_tile] = temp

    def move_up(self, cur_tile):
        if cur_tile-3 >= 0:
            if self.board[cur_tile-3] == -1:
                self.swap_tiles(cur_tile-3, cur_tile)

    def move_down(self, cur_tile):
        if cur_tile+3 <= 9:
            if self.board[cur_tile+3] == -1:
                self.swap_tiles(cur_tile+3, cur_tile)

    def move_right(self, cur_tile):
        if cur_tile+1 <= 9:
            if self.board[cur_tile+1] == -1:
                self.swap_tiles(cur_tile+1, cur_tile)

    def move_left(self, cur_tile):
        if cur_tile-1 >= 0:
            print("here1")
            if self.board[cur_tile-1] == -1:
                print("here2")
                self.swap_tiles(cur_tile-1, cur_tile)

    def goal_state(self):
        if self.board == [-1,1,2,3,4,5,6,7,8]:
            print("You Win!")
            return True
        return False

    def print_board(self):
        count = 1
        for x in self.board:
            if x == -1:
                print(" ", end= " | ")
            else:
                print(x, end= " | ")
            if count % 3 == 0:
                print("\n")
            count += 1

    def calculate_misplaced_heuristic(self):
        count = 0
        for x in range(len(self.board)):
            if self.board[x] == -1:
                continue
            if self.board[x] != x:
                count = count + 1
        return count

    def calculate_x_coor(index):
        x_cor = index%3
        return x_cor

    def calculate_y_coor(index):
        y_cor = index/3
        return y_cor

    def calculate_difference(self, goal_index, cur_index):
        goal_x = self.calculate_x_coor(goal_index)
        goal_y = self.calculate_y_coor(goal_index)
        cur_x = self.calculate_x_coor(cur_index)
        cur_y = self.calculate_y_coor(cur_index)
        dif_x = abs(goal_x - cur_x)
        dif_y = abs(cur_x - cur_y)
        return dif_x + dif_y

    def check_validity(self):
        valid_counter = 0
        for x in range(len(self.board)):
            if self.board[x] == -1:
                continue
            for y in range(0,x):
                if self.board[y] == -1:
                    continue
                if self.board[y] < self.board[x]:
                    valid_counter += 1
        if valid_counter % 2 == 0:
            return True
        else:
            return False

    def create_graphs(self, repeat):
        graph_list = []

        while len(graph_list) < repeat:
            self.shuffle()
            if self.check_validity() == True:
                graph_list.append(self.board[:])

        return graph_list

    # def calculate_manhattan_heuristic(self):


myPuzzle = Puzzle8()
graphs = myPuzzle.shuffle()
# print(graphs)
valids = myPuzzle.calculate_misplaced_heuristic()
# print(valids)



