# a1.py

from search import *
import random


def make_rand_8puzzle():
    problem_inst = EightPuzzle((1, 2, 3, 4, 5, 6, 7, 8, 0),
                               (1, 2, 3, 4, 5, 6, 7, 8, 0))

    my_state = problem_inst.initial
    #print(problem_inst.initial)
    #print(EightPuzzle.actions(problem_inst, my_state))

    #print(problem_inst.actions(my_state))
    for i in range(40):
        my_actions = EightPuzzle.actions(problem_inst, my_state)
        my_state = EightPuzzle.result(problem_inst, my_state,
                                      random.choice(my_actions))
        #print(my_state)
    #print(problem_inst.check_solvability(my_state))
    return EightPuzzle(my_state, (1, 2, 3, 4, 5, 6, 7, 8, 0))


def display(state):
    print(state)
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


prob_inst = make_rand_8puzzle()

display(prob_inst.initial)