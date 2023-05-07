#!/usr/bin/env python3
"""
mesures de performances.
"""

from time import time
from sys import argv
from os import system
import matplotlib.pyplot as plt
from generator import nb_points

plt.figure()
distances = [0.001 * i for i in range(100)]
execution_time = []
for i, distance in enumerate(distances):
    t = time()
    system(f".././connectes_{argv[1]}.py {distance} test_18.pts")
    execution_time.append(time() - t)
plt.plot(distances, execution_time, "r-")
plt.xlabel("Distance")
plt.ylabel("Execution time (s)")
plt.savefig(f"distance_time_{argv[1]}.pdf")
plt.show()
