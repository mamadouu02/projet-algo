#!/usr/bin/env python3
"""
generation de fichiers test.
"""

from os import system
from random import random, seed

def main():
    """
    genere des fichiers test.
    """
    seed()
    system("rm test*")
    nb_points = [i * 10**k for k in range(1, 5) for i in range(1, 10)]
    for i, n in enumerate(nb_points):
        fichier = open(f"test_{i}.pts", "w")
        fichier.write(f"{0.05}\n")
        for _ in range(n):
            fichier.write(f"{random()}, {random()}\n")
        fichier.close()


main()
