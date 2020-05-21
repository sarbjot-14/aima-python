# a1.py

from search import *
import random
import time


class DuckPuzzle(Problem):
    """ The problem of sliding tiles numbered from 1 to 8 on a 3x3 board, where one of the
    squares is a blank. A state is represented as a tuple of length 9, where  element at
    index i represents the tile number  at index i (0 if it's an empty square) """
    def __init__(self, initial, goal=(1, 2, 3, 4, 5, 6, 7, 8, 0)):
        """ Define goal state and initialize a problem """
        super().__init__(initial, goal)

    def find_blank_square(self, state):
        """Return the index of the blank square in a given state"""
        ##print("0 is in spot ", state.index(0), "of ", state)
        return state.index(0)

    def actions(self, state):
        """ Return the actions that can be executed in the given state.
        The result would be a list, since there are only four possible actions
        in any given state of the environment """

        possible_actions = ['UP', 'DOWN', 'LEFT', 'RIGHT']
        index_blank_square = self.find_blank_square(state)
        ##print("blank is at ", index_blank_square)
        if index_blank_square == 0:
            possible_actions.remove('UP')

            possible_actions.remove('LEFT')
        elif index_blank_square == 1:

            possible_actions.remove('UP')
            possible_actions.remove('RIGHT')
        elif index_blank_square == 2:
            possible_actions.remove('LEFT')
            possible_actions.remove('DOWN')

        elif index_blank_square == 3:
            pass
        elif index_blank_square == 4:
            possible_actions.remove('UP')

        elif index_blank_square == 5:
            possible_actions.remove('UP')
            possible_actions.remove('RIGHT')
        elif index_blank_square == 6:
            possible_actions.remove('LEFT')
            possible_actions.remove('DOWN')

        elif index_blank_square == 7:
            possible_actions.remove('DOWN')

        elif index_blank_square == 8:
            possible_actions.remove('RIGHT')
            possible_actions.remove('DOWN')
        """
        if index_blank_square % 3 == 0:
            possible_actions.remove('LEFT')
        if index_blank_square < 3:
            possible_actions.remove('UP')
        if index_blank_square % 3 == 2:
            possible_actions.remove('RIGHT')
        if index_blank_square > 5:
            possible_actions.remove('DOWN')
        """
        return possible_actions

    def result(self, state, action):
        """ Given state and action, return a new state that is the result of the action.
        Action is assumed to be a valid action in the state """

        #state = (4, 5, 6, 7, 2, 3, 8, 1, 0)
        #display_duck(state)
        # blank is the index of the blank square
        blank = self.find_blank_square(state)

        new_state = list(state)

        #action = "LEFT"
        '''
        delta = {'UP': -3, 'DOWN': 3, 'LEFT': -1, 'RIGHT': 1}
        neighbor = blank + delta[action]
        '''
        # all ups

        if (blank == 2 or blank == 3) and (action == 'UP'):
            neighbor = blank - 2
        if (blank == 6 or blank == 7 or blank == 8) and (action == 'UP'):
            neighbor = blank - 3

        # all down
        if (blank == 0 or blank == 1) and (action == 'DOWN'):
            neighbor = blank + 2

        if (blank == 3 or blank == 4 or blank == 5) and (action == 'DOWN'):
            neighbor = blank + 3

        # all right
        if (blank == 0 or blank == 2) and (action == 'RIGHT'):
            neighbor = blank + 1

        if (blank == 3 or blank == 4 or blank == 6
                or blank == 7) and (action == 'RIGHT'):
            neighbor = blank + 1
        # all left
        if (blank == 1 or blank == 3) and (action == 'LEFT'):
            neighbor = blank - 1

        if (blank == 4 or blank == 5 or blank == 7
                or blank == 8) and (action == 'LEFT'):
            neighbor = blank - 1

        #print("blank is ", blank, "action is ", action, "neighbor is ",neighbor)
        new_state[blank], new_state[neighbor] = new_state[neighbor], new_state[
            blank]
        #display_duck(new_state)
        return tuple(new_state)

    def goal_test(self, state):
        """ Given a state, return True if state is a goal state or False, otherwise """

        return state == self.goal

    def check_solvability(self, state):
        """ Checks if the given state is solvable """

        inversion = 0
        for i in range(len(state)):
            for j in range(i + 1, len(state)):
                if (state[i] > state[j]) and state[i] != 0 and state[j] != 0:
                    inversion += 1

        return inversion % 2 == 0

    def h(self, node):
        """ Return the heuristic value for a given state. Default heuristic function used is 
        h(n) = number of misplaced tiles """
        """
        print(node.state)
        print(self.goal)
        print(sum(s != g for (s, g) in zip(node.state, self.goal)))
        """
        return sum(s != g for (s, g) in zip(node.state, self.goal))


def make_rand_8puzzle():
    problem_inst = EightPuzzle((1, 2, 3, 4, 5, 6, 7, 8, 0),
                               (1, 2, 3, 4, 5, 6, 7, 8, 0))

    my_state = problem_inst.initial

    for i in range(100):
        my_actions = EightPuzzle.actions(problem_inst, my_state)
        my_state = EightPuzzle.result(problem_inst, my_state,
                                      random.choice(my_actions))
        #print(my_state)
    #print(problem_inst.check_solvability(my_state))
    return EightPuzzle(my_state, (1, 2, 3, 4, 5, 6, 7, 8, 0))


def make_rand_duckpuzzle():
    problem_inst = DuckPuzzle((1, 2, 3, 4, 5, 6, 7, 8, 0),
                              (1, 2, 3, 4, 5, 6, 7, 8, 0))

    my_state = problem_inst.initial
    #display_duck(my_state)

    for i in range(200):
        my_actions = DuckPuzzle.actions(problem_inst, my_state)
        #print(my_actions)
        my_move = random.choice(my_actions)
        #print("my move is ", my_move)
        my_state = DuckPuzzle.result(problem_inst, my_state, my_move)
        #display_duck(my_state)

        #print(my_state)
    #print(problem_inst.check_solvability(my_state))
    return DuckPuzzle(my_state, (1, 2, 3, 4, 5, 6, 7, 8, 0))


def display(state):
    #print(state)
    k = 1
    for i in range(9):
        #print(k)
        #print(k % 3)
        if state[i] == 0:
            print("* ", end="")
        else:
            print(state[i], " ", end="")
        if k % 3 == 0:
            print("")
        k += 1
    return


def display_duck(state):
    #print(state)
    def print_tile(tile):
        if tile == 0:
            print("* ", end="")
        else:
            print(tile, " ", end="")

    print_tile(state[0])
    print_tile(state[1])

    print("\n", end="")
    for i in range(2, 6):

        print_tile(state[i])
    print("\n   ", end="")
    for i in range(6, 9):
        print_tile(state[i])
    print("\n")

    return


## Manhattan distance
def manattan_dist(node):

    state = node.state
    mhd = 0

    table_patterns = {
        1: [0, 1, 2, 1, 2, 3, 2, 3, 4],
        2: [1, 0, 1, 2, 1, 2, 3, 2, 3],
        3: [2, 1, 0, 3, 2, 1, 4, 3, 2],
        4: [1, 2, 3, 0, 1, 2, 1, 2, 3],
        5: [2, 1, 2, 1, 0, 1, 2, 1, 2],
        6: [3, 2, 1, 2, 1, 0, 3, 2, 1],
        7: [2, 3, 4, 1, 2, 3, 0, 1, 2],
        8: [3, 2, 3, 2, 1, 2, 1, 0, 1],
        0: [4, 3, 2, 3, 2, 1, 2, 1, 0]
    }

    for i in range(len(state)):
        mhd = table_patterns[state[i]][i] + mhd
    return mhd


    ## Manhattan distance
def manattan_dist_duck(node):

    state = node.state
    mhd = 0

    table_patterns = {
        1: [0, 1, 1, 2, 3, 4, 3, 4, 5],
        2: [1, 0, 2, 1, 2, 3, 2, 3, 4],
        3: [1, 2, 0, 1, 2, 3, 2, 3, 4],
        4: [1, 1, 1, 0, 1, 2, 1, 2, 3],
        5: [3, 2, 2, 1, 0, 1, 2, 1, 2],
        6: [4, 3, 3, 2, 1, 0, 3, 2, 1],
        7: [3, 2, 2, 1, 2, 3, 0, 1, 2],
        8: [4, 3, 3, 2, 1, 2, 1, 0, 1],
        0: [5, 4, 4, 3, 2, 1, 2, 1, 0]
    }

    for i in range(len(state)):
        mhd = table_patterns[state[i]][i] + mhd
    return mhd


def misplaced_and_manattan_dist(node):
    state = node.state
    mhd = 0

    table_patterns = {
        1: [0, 1, 2, 1, 2, 3, 2, 3, 4],
        2: [1, 0, 1, 2, 1, 2, 3, 2, 3],
        3: [2, 1, 0, 3, 2, 1, 4, 3, 2],
        4: [1, 2, 3, 0, 1, 2, 1, 2, 3],
        5: [2, 1, 2, 1, 0, 1, 2, 1, 2],
        6: [3, 2, 1, 2, 1, 0, 3, 2, 1],
        7: [2, 3, 4, 1, 2, 3, 0, 1, 2],
        8: [3, 2, 3, 2, 1, 2, 1, 0, 1],
        0: [4, 3, 2, 3, 2, 1, 2, 1, 0]
    }

    for i in range(len(state)):
        mhd = table_patterns[state[i]][i] + mhd

    misplaced = sum(s != g
                    for (s, g) in zip(node.state, (1, 2, 3, 4, 5, 6, 7, 8, 0)))

    return max(mhd, misplaced)


def misplaced_and_manattan_duck(node):
    state = node.state
    mhd = 0

    table_patterns = {
        1: [0, 1, 1, 2, 3, 4, 3, 4, 5],
        2: [1, 0, 2, 1, 2, 3, 2, 3, 4],
        3: [1, 2, 0, 1, 2, 3, 2, 3, 4],
        4: [1, 1, 1, 0, 1, 2, 1, 2, 3],
        5: [3, 2, 2, 1, 0, 1, 2, 1, 2],
        6: [4, 3, 3, 2, 1, 0, 3, 2, 1],
        7: [3, 2, 2, 1, 2, 3, 0, 1, 2],
        8: [4, 3, 3, 2, 1, 2, 1, 0, 1],
        0: [5, 4, 4, 3, 2, 1, 2, 1, 0]
    }

    for i in range(len(state)):
        mhd = table_patterns[state[i]][i] + mhd

    misplaced = sum(s != g
                    for (s, g) in zip(node.state, (1, 2, 3, 4, 5, 6, 7, 8, 0)))

    return max(mhd, misplaced)


## Question 2
def question_two():
    rand_inst = []
    for i in range(10):

        rand_inst.append(make_rand_8puzzle())

    for i in range(10):
        ##print(i)
        start_time = time.time()
        #display(rand_inst[i].initial)
        print("#", i, ", ", end="")
        final_node = astar_search(rand_inst[i], None, display)
        print(", ", len(final_node.solution()), end="")
        #print(final_node.state)
        elapsed_time = time.time() - start_time

        print(", ", elapsed_time)

    print(" ")
    for i in range(10):
        ##print(i)
        start_time = time.time()
        #display(rand_inst[i].initial)
        print("#", i, ", ", end="")
        final_node = astar_search(rand_inst[i], manattan_dist, display)
        print(", ", len(final_node.solution()), end="")
        #print(final_node.state)
        elapsed_time = time.time() - start_time

        print(", ", elapsed_time)
    print(" ")
    for i in range(10):
        ##print(i)
        start_time = time.time()
        #display(rand_inst[i].initial)
        print("#", i, ", ", end="")
        final_node = astar_search(rand_inst[i], misplaced_and_manattan_dist,
                                  display)
        print(", ", len(final_node.solution()), end="")
        #print(final_node.state)
        elapsed_time = time.time() - start_time

        print(", ", elapsed_time)
    return


def question_three():
    #duck = make()

    rand_inst = []
    for i in range(10):
        rand_inst.append(make_rand_duckpuzzle())

    for i in range(10):
        ##print(i)
        start_time = time.time()
        #display(rand_inst[i].initial)
        print("#", i, ", ", end="")
        final_node = astar_search(rand_inst[i], None, display_duck)
        print(", ", len(final_node.solution()), end="")

        elapsed_time = time.time() - start_time

        print(", ", elapsed_time)

    print(" ")
    print(" ")
    for i in range(10):
        ##print(i)
        start_time = time.time()
        #display(rand_inst[i].initial)
        print("#", i, ", ", end="")
        final_node = astar_search(rand_inst[i], manattan_dist_duck, display)
        print(", ", len(final_node.solution()), end="")
        #print(final_node.state)
        elapsed_time = time.time() - start_time

        print(", ", elapsed_time)
    print(" ")
    print(" ")
    for i in range(10):
        ##print(i)
        start_time = time.time()
        #display(rand_inst[i].initial)
        print("#", i, ", ", end="")
        final_node = astar_search(rand_inst[i], misplaced_and_manattan_duck,
                                  display)
        print(", ", len(final_node.solution()), end="")
        #print(final_node.state)
        elapsed_time = time.time() - start_time

        print(", ", elapsed_time)
    #display_duck(duck.initial)

    return


question_three()
#question_two()