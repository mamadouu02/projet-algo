#!/usr/bin/env python3
"""
mesures de performances.
"""

from time import time
from sys import argv
from os import system
import matplotlib.pyplot as plt
from generator import nb_points


def main():
    """
    trace une courbe de performances.
    """
    plt.figure()
    for method in ["list", "dict", "tree"]:
        execution_time = []
        for i, _ in enumerate(nb_points):
            t = time()
            system(f".././connectes_{method}.py test_{i}.pts")
            execution_time.append(time() - t)
        plt.plot(nb_points, execution_time, label=method)
    plt.xlabel("Number of points")
    plt.ylabel("Execution time (s)")
    plt.legend()
    plt.show()


main()
