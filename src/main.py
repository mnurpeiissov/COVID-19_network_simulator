from network_sim import NetworkSim

import numpy as np


T = np.zeros((17,17))  # transition matrix 17x17

total_country = NetworkSim(trans_matrix = T)

print(sim.T)

sim_len = 1000

for i in range(sim_len):

    simulate_each_city()

    if i%100 :
        total_country.update_nodes_init()
