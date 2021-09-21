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

    def random_moves(self, move_num):
        while move_num >= 0:
            rand = random.randint(1,4)
            empt = self.board.index(-1)
            if rand == 1:
                move_num = move_num -1
                self.move_left(empt)
            if rand == 2:
                move_num = move_num -1
                self.move_right(empt)
            if rand == 3:
                move_num = move_num -1
                self.move_down(empt)
            if rand == 4:
                move_num = move_num -1
                self.move_up(empt)

    def update_board(self, new_board):
        self.board = new_board.copy()





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

# myPuzzle.shuffle()
# mygraph = myPuzzle.random_moves(10)
# myPuzzle.random_moves(10)

# mygraph = [1,4,2,3,7,5,6,8,-1]
# mygraph = [1,-1,2,3,4,5,6,7,8]
# myPuzzle.board = [1,4,2,3,7,5,6,8,-1]
# myPuzzle.board = [1,-1,4,3,7,2,6,8,5]
# myPuzzle.board = [3,1,4,7,-1,2,6,8,5]
# myPuzzle.board = [3,1,4,7,2,-1,6,8,5] # 11 sol
# myPuzzle.board = [3,1,4,7,2,5,6,8,-1]
# myPuzzle.board = [3,1,4,7,2,5,-1,6,8]
# myPuzzle.board = [3,1,4,7,2,5,-1,6,8]
# print(mygraph)
counter = 0
ind_zero = myPuzzle.board.index(-1)
man_heur = myPuzzle.calculate_manhattan_heuristic()
heapq.heappush(queue_manh,tuple((man_heur, myPuzzle.board,0)))
searched_graphs = []

while len(queue_manh):
    heapq.heapify(queue_manh)
    pop_val = heapq.heappop(queue_manh)

    if pop_val[1] == [-1,1,2,3,4,5,6,7,8]:
        print(counter, "solution length")
        print(counter)
        break

    for x in searched_graphs:
        if x == pop_val[1]:
            continue

    searched_graphs.append(pop_val[1])
    myPuzzleUp.board = pop_val[1].copy()
    myPuzzleDown.board = pop_val[1].copy()
    myPuzzleRight.board = pop_val[1].copy()
    myPuzzleLeft.board = pop_val[1].copy()

    ind_zero = myPuzzleUp.board.index(-1)
    print(pop_val, ",manh heur")
    counter += 1
    pcost = pop_val[2]
    if(myPuzzleDown.move_down(ind_zero)):
        print(myPuzzleDown.board,"puzzle_down")
        manhattan_heur1 = myPuzzleDown.calculate_manhattan_heuristic()
        heapq.heappush(queue_manh, tuple((manhattan_heur1+pcost, myPuzzleDown.board, pcost+1)))

    if(myPuzzleUp.move_up(ind_zero)):
        print(myPuzzleUp.board,"puzzle_up")
        manhattan_heur2 = myPuzzleUp.calculate_manhattan_heuristic()
        heapq.heappush(queue_manh, tuple((manhattan_heur2+pcost, myPuzzleUp.board, pcost+1)))

    if(myPuzzleRight.move_right(ind_zero)):
        print(myPuzzleRight.board,"puzzle_right")
        manhattan_heur3 = myPuzzleRight.calculate_manhattan_heuristic()
        heapq.heappush(queue_manh, tuple((manhattan_heur3+pcost, myPuzzleRight.board, pcost+1)))

    if(myPuzzleLeft.move_left(ind_zero)):
        print(myPuzzleLeft.board,"puzzle_left")
        manhattan_heur4 = myPuzzleLeft.calculate_manhattan_heuristic()
        heapq.heappush(queue_manh, tuple((manhattan_heur4+pcost, myPuzzleLeft.board, pcost+1)))



# print(searched_graphs, "searched graphs")

