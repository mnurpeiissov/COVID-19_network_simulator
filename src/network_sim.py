import numpy as np

class NetworkSim:
    def __init__(self, trans_matrix):

        self.T = trans_matrix
        self.states = ['node 1', 'node 2'] # etc
        self.states_num = 17

    def update_nodes_init(self):
        for i in range(self.states_num):
            # update init params of the city

    def visualise_states(self):
        pass
