#!/usr/bin/env python3
"""
mesures de performances
"""

from time import time
from sys import argv, setrecursionlimit
import matplotlib.pyplot as plt

import connectes


def main():
    """
    trace une courbe de performances
    """
    nb_points = []
    execution_time = []

    for instance in argv[1:]:
        distance, points = connectes.load_instance(instance)
        nb_points.append(len(points))
        t_1 = time()
        connectes.print_components_sizes(distance, points)
        t_2 = time()
        execution_time.append(t_2 - t_1)

    plt.plot(nb_points, execution_time, 'o-')
    plt.xlabel("Number of points")
    plt.ylabel("Execution time (s)")
    plt.show()


setrecursionlimit(1000000)
main()
