# Name: pa1.py
# Author: Rodolfo Lopez
# Date:09/30/2021
# Description: DFA simulation

import re
import sys


class DFA:
    """Simulates a DFA"""

    # class variable used to recognize transition pattern from file
    state_reg_exp = re.compile("\d* '.' \d*")

    def __init__(self, filename):
        """
        Initializes DFA from the file whose name is
        filename
        """

        # open infile
        self.filename = open(filename, "r")

        # read number of states (not necessary)
        self.num_states = self.filename.readline().rstrip()

        # read alphabet into list
        self.alpha = list(self.filename.readline().rstrip())

        # reads transition function into 2D list
        self.states = []
        self.line = self.filename.readline()
        while DFA.state_reg_exp.match(self.line):
            self.line_list = self.line.split()
            # nested list contains current state, symbol, and next state
            self.states.append(
                [self.line_list[0], self.line_list[1][1], self.line_list[2]]
            )
            # on last iteration read start state
            self.start_state = self.line = self.filename.readline().rstrip()

        # read accept states into list
        self.accept_states = self.filename.readline().split()

        # close infile
        self.filename.close()

        # before simulation
        self.next_state = None
        self.final_state = None

    def simulate(self, str):
        """
        Simulates the DFA on input str.  Returns
        True if str is in the language of the DFA,
        and False if not.
        """
        # start of simulation
        self.num_transitions = 0
        for sym in str:
            # unrecognized symbol
            if sym not in self.alpha:
                return False
            else:
                # pass start state initially to transition func
                if self.num_transitions == 0:
                    self.transition(self.start_state, sym)
                # pass next state to transition func
                else:
                    self.transition(self.next_state, sym)

        # after all symbols are read set final state
        self.final_state = self.next_state

        # accepting final state
        if self.final_state in self.accept_states:
            return True
        else:
            # rejecting final state
            return False

    def transition(self, cur_state, sym):
        # increment transition
        self.num_transitions += 1
        for trans in self.states:
            # current state matches with current symbol
            if (trans[0] == cur_state) and (trans[1] == sym):
                self.next_state = trans[2]  # go to next state
