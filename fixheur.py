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


print("started")
gtwo = []
gfour = []
gsix = []
geight =[]
gten=[]
gtwelve=[]
gfourteen=[]
gsixteen=[]
geighteen=[]
gtwenty=[]
gtwentytwo=[]
gtwentyfour=[]

for xloop in range(5000):
    queue_manh = []
    pcost = 0
    nodes_searched = 0
    graphs_generated = 0
    myPuzzle.board =[-1,1,2,3,4,5,6,7,8]
    myPuzzle.random_moves(30)
    ind_zero = myPuzzle.board.index(-1)
    man_heur = myPuzzle.calculate_manhattan_heuristic()
    heapq.heappush(queue_manh,tuple((man_heur, myPuzzle.board,0)))
    searched_graphs = []
    searched_nodes = []
    length_queue = 0
    while len(queue_manh):
        heapq.heapify(queue_manh)
        pop_val = heapq.heappop(queue_manh)

        if pop_val[1] == [-1,1,2,3,4,5,6,7,8]:
#             print(nodes_searched, "solution length")
#             print(nodes_searched)
            break

        if pop_val in searched_nodes:
            continue
        # print("searched graphs: ", searched_graphs)
        # for x in searched_graphs:
        #     if x == pop_val[1]:
        #         continue
        searched_nodes.append(pop_val)
        # searched_graphs.append(pop_val[1])
        myPuzzleUp.board = pop_val[1].copy()
        myPuzzleDown.board = pop_val[1].copy()
        myPuzzleRight.board = pop_val[1].copy()
        myPuzzleLeft.board = pop_val[1].copy()

        ind_zero = myPuzzleUp.board.index(-1)
        print(pop_val, ",manh heur and graph num: ",xloop)
        nodes_searched += 1
        pcost = pop_val[2]
        if(myPuzzleDown.move_down(ind_zero)):
            graphs_generated += 1
            # print(myPuzzleDown.board,"puzzle_down")
            manhattan_heur1 = myPuzzleDown.calculate_manhattan_heuristic()
            heapq.heappush(queue_manh, tuple((manhattan_heur1+pcost, myPuzzleDown.board, pcost+1)))

        if(myPuzzleUp.move_up(ind_zero)):
            graphs_generated += 1
            # print(myPuzzleUp.board,"puzzle_up")
            manhattan_heur2 = myPuzzleUp.calculate_manhattan_heuristic()
            heapq.heappush(queue_manh, tuple((manhattan_heur2+pcost, myPuzzleUp.board, pcost+1)))

        if(myPuzzleRight.move_right(ind_zero)):
            graphs_generated += 1
            # print(myPuzzleRight.board,"puzzle_right")
            manhattan_heur3 = myPuzzleRight.calculate_manhattan_heuristic()
            heapq.heappush(queue_manh, tuple((manhattan_heur3+pcost, myPuzzleRight.board, pcost+1)))

        if(myPuzzleLeft.move_left(ind_zero)):
            graphs_generated += 1
            # print(myPuzzleLeft.board,"puzzle_left")
            manhattan_heur4 = myPuzzleLeft.calculate_manhattan_heuristic()
            heapq.heappush(queue_manh, tuple((manhattan_heur4+pcost, myPuzzleLeft.board, pcost+1)))
    length_queue = len(queue_manh)
    # print(pcost,"solution length")
    # print(nodes_searched, "nodes searched")

    if pcost == 2:
        gtwo.append(graphs_generated)

    if pcost == 4:
        gfour.append(graphs_generated)

    if pcost == 6:
        gsix.append(graphs_generated)

    if pcost == 8:
        geight.append(graphs_generated)

    if pcost == 10:
        gten.append(graphs_generated)

    if pcost == 12:
        gtwelve.append(graphs_generated)

    if pcost == 14:
        gfourteen.append(graphs_generated)

    if pcost == 16:
        gsixteen.append(graphs_generated)

    if pcost == 18:
        geighteen.append(graphs_generated)

    if pcost == 20:
        gtwenty.append(graphs_generated)

    if pcost == 22:
        gtwentytwo.append(graphs_generated)

    if pcost == 24:
        gtwentyfour.append(graphs_generated)

#     print(graphs_generated,"nodes generated")

# print(gtwo, "this is gtwo")
# print(gfour, "this is gfour")
# print(gsix, "this is gsix")
# print(g, "this is geight")
# print(gtwo, "this is gten")
# print(gfour, "this is gevelen")

print()

sumgtwo = 0
sumgfour = 0
sumgsix = 0
sumgeight = 0
sumgten = 0
sumgtwelve = 0
sumgfourteen=0
sumgsixteen=0
sumgeighteen=0
sumgtwenty=0
sumgtwentytwo=0
sumgtwentyfour=0

for x in gtwo:
    sumgtwo += x

for x in gfour:
    sumgfour += x

for x in gsix:
    sumgsix += x

for x in geight:
    sumgeight += x

for x in gten:
    sumgten += x

for x in gtwelve:
    sumgtwelve += x

for x in gfourteen:
    sumgfourteen += x

for x in gsixteen:
    sumgsixteen += x

for x in geighteen:
    sumgeighteen += x

for x in gtwenty:
    sumgtwenty += x

for x in gtwentytwo:
    sumgtwentytwo += x

for x in gtwentyfour:
    sumgtwentyfour += x

if len(gtwo) !=0:
    print(gtwo, "this is gtwo and average: ", sumgtwo/len(gtwo) , "and length is: ", len(gtwo))
if len(gfour) !=0:
    print(gfour, "this is gfour and average: ", sumgfour/len(gfour) , "and length is: ", len(gfour))
if len(gsix) !=0:
    print(gsix, "this is gsix and average: ", sumgsix/len(gsix) , "and length is: ", len(gsix))
if len(geight) !=0:
    print(geight, "this is geight and average: ", sumgeight/len(geight) , "and length is: ", len(geight))
if len(gten) !=0:
    print(gten, "this is gten and average: ", sumgten/len(gten), "and length is: ", len(gten))
if len(gtwelve) !=0:
    print(gtwelve, "this is gtwelve and average: ", sumgtwelve/len(gtwelve) , "and length is: ", len(gtwelve))

if len(gfourteen) !=0:
    print(gfourteen, "this is gfourteen and average: ", sumgfourteen/len(gfourteen) , "and length is: ", len(gfourteen))
if len(gsixteen) !=0:
    print(gsixteen, "this is gsixteen and average: ", sumgsixteen/len(gsixteen) , "and length is: ", len(gsixteen))
if len(geighteen) !=0:
    print(geighteen, "this is geighteen and average: ", sumgeighteen/len(geighteen) , "and length is: ", len(geighteen))
if len(gtwenty) !=0:
    print(gtwenty, "this is gtwenty and average: ", sumgtwenty/len(gtwenty) , "and length is: ", len(gtwenty))
if len(gtwentytwo) !=0:
    print(gtwentytwo, "this is gtwentytwo and average: ", sumgtwentytwo/len(gtwentytwo), "and length is: ", len(gtwentytwo))
if len(gtwentyfour) !=0:
    print(gtwentyfour, "this is gtwentyfour and average: ", sumgtwentyfour/len(gtwentyfour) , "and length is: ", len(gtwentyfour))

