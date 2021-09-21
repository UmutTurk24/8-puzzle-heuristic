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

heapqueue, tuple. f values and board

 """
import random
import math
import heapq

class Puzzle8:

    def __init__(self):
        self.board = board = [-1,1,2,3,4,5,6,7,8]
        self.queue_manh = queue_manh = []
        self.queue_misp = queue_misp = []


    def shuffle(self):
        random.shuffle(self.board)
        return self.board

    def swap_tiles(self, target_tile, cur_tile):
        temp = self.board[target_tile]
        self.board[target_tile] = self.board[cur_tile]
        self.board[cur_tile] = temp

    def move_up(self, cur_tile):
        if cur_tile-3 >= 0:
            self.swap_tiles(cur_tile-3, cur_tile)
            return True
        else:
            return False

    def move_down(self, cur_tile):
        if cur_tile+3 <= 8:
            self.swap_tiles(cur_tile+3, cur_tile)
            return True
        else:
            return False

    def move_right(self, cur_tile):
        if cur_tile+1 <= 8:
            self.swap_tiles(cur_tile+1, cur_tile)
            return True
        else:
            return False

    def move_left(self, cur_tile):
        if cur_tile-1 >= 0:
            self.swap_tiles(cur_tile-1, cur_tile)
            return True
        else:
            return False

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

    def calculate_x_coor(self, index):
        x_cor = index%3
        return x_cor

    def calculate_y_coor(self, index):
        y_cor = math.floor(index/3)
        return y_cor

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

    def calculate_difference(self, goal_index, cur_index):
        goal_x = self.calculate_x_coor(goal_index)
        goal_y = self.calculate_y_coor(goal_index)
        cur_x = self.calculate_x_coor(cur_index)
        cur_y = self.calculate_y_coor(cur_index)
        dif_x = abs(goal_x - cur_x)
        dif_y = abs(goal_y - cur_y)
        return dif_x + dif_y

    def calculate_manhattan_heuristic(self):
        diff = 0
        for x in range(len(self.board)):
            if self.board[x] == -1:
                continue
            if x != self.board[x]:
                ind_val = self.board[x]
                diff = diff + self.calculate_difference(ind_val, x)
        return diff

    def update_board(self, new_board):
        self.board = new_board.copy()

    # def move_around_manh(self):
    #     ind_zero = self.board.index(-1)
    #     self.cur_board1 = self.board.copy()
    #     self.cur_board2 = self.board.copy()
    #     self.cur_board3 = self.board.copy()
    #     self.cur_board4 = self.board.copy()
    #     print(self.cur_board1)
    #     if (self.move_up(self.cur_board1[ind_zero])):
    #         manhattan_heur = self.calculate_manhattan_heuristic()
    #         self.queue_manh.append(tuple((manhattan_heur, self.cur_board1)))
    #     if (self.move_right(self.cur_board2[ind_zero])):
    #         manhattan_heur = self.calculate_manhattan_heuristic()
    #         self.queue_manh.append(tuple((manhattan_heur, self.cur_board2)))
    #     if (self.move_left(self.cur_board3[ind_zero])):
    #         manhattan_heur = self.calculate_manhattan_heuristic()
    #         self.queue_manh.append(tuple((manhattan_heur, self.cur_board3)))
    #     if (self.move_down(self.cur_board4[ind_zero])):
    #         manhattan_heur = self.calculate_manhattan_heuristic()
    #         self.queue_manh.append(tuple((manhattan_heur, self.cur_board4)))
    #     return heapq.heapify(self.queue_manh)

    # def move_around_misp(self):
    #     ind_zero = self.board.index(-1)

    #     cur_board1, cur_board2, cur_board3, cur_board4 = self.board.copy()
    #     if (self.move_up(cur_board1[ind_zero])):
    #         misplaced_heur = self.calculate_misplaced_heuristic()
    #         self.queue_misp.append(tuple((misplaced_heur, cur_board1)))
    #     if (self.move_up(cur_board2[ind_zero])):
    #         misplaced_heur = self.calculate_misplaced_heuristic()
    #         self.queue_misp.append(tuple((misplaced_heur, cur_board2)))
    #     if (self.move_up(cur_board3[ind_zero])):
    #         misplaced_heur = self.calculate_misplaced_heuristic()
    #         self.queue_misp.append(tuple((misplaced_heur, cur_board3)))
    #     if (self.move_up(cur_board4[ind_zero])):
    #         misplaced_heur = self.calculate_misplaced_heuristic()
    #         self.queue_misp.append(tuple((misplaced_heur, cur_board4)))
    #     return heapq.heapify(self.queue_misp)





"""
For each possible move the blank space can do in 8puzzle:
    create a heuristic for each possibility
    store them in a pri queue - how to keep track of which one is which?
    do we have to create a node-graph? or is enqueuing enough?
 """

myPuzzle = Puzzle8()

myPuzzleUp = Puzzle8()
myPuzzleDown = Puzzle8()
myPuzzleRight = Puzzle8()
myPuzzleLeft = Puzzle8()
queue_manh = []

myPuzzle.shuffle()
mygraph = myPuzzle.create_graphs(1)
# mygraph = [1,4,2,3,7,5,6,-1,8]
# mygraph = [1,-1,2,3,4,5,6,7,8]
myPuzzle.board = mygraph[0].copy()
print(mygraph)
counter = 0
ind_zero = myPuzzle.board.index(-1)
man_heur = myPuzzle.calculate_manhattan_heuristic()
heapq.heappush(queue_manh,tuple((man_heur, myPuzzle.board)))
# searched_graphs = []

while len(queue_manh) < 200:
    heapq.heapify(queue_manh)
    pop_val = heapq.heappop(queue_manh)


    if pop_val[1] == [-1,1,2,3,4,5,6,7,8]:
        print("Found a solution")
        print(counter)
        break

    myPuzzleUp.board = pop_val[1].copy()
    myPuzzleDown.board = pop_val[1].copy()
    myPuzzleRight.board = pop_val[1].copy()
    myPuzzleLeft.board = pop_val[1].copy()

    ind_zero = myPuzzleUp.board.index(-1)
    print(pop_val[0], ",manh heur")

    if(myPuzzleDown.move_down(ind_zero)):
        print(myPuzzleDown.board,"puzzle_down")
        manhattan_heur = myPuzzleDown.calculate_manhattan_heuristic()
        heapq.heappush(queue_manh,tuple((manhattan_heur, myPuzzleDown.board)))

    if(myPuzzleUp.move_up(ind_zero)):
        print(myPuzzleUp.board,"puzzle_up")
        manhattan_heur = myPuzzleUp.calculate_manhattan_heuristic()
        heapq.heappush(queue_manh,tuple((manhattan_heur, myPuzzleUp.board)))

    if(myPuzzleRight.move_right(ind_zero)):
        print(myPuzzleRight.board,"puzzle_right")
        manhattan_heur = myPuzzleRight.calculate_manhattan_heuristic()
        heapq.heappush(queue_manh,tuple((manhattan_heur, myPuzzleRight.board)))

    if(myPuzzleLeft.move_left(ind_zero)):
        print(myPuzzleLeft.board,"puzzle_left")
        manhattan_heur = myPuzzleLeft.calculate_manhattan_heuristic()
        heapq.heappush(queue_manh,tuple((manhattan_heur, myPuzzleLeft.board)))

    counter =+ 1

# print(counter)


