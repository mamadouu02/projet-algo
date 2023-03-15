#!/usr/bin/env python3
"""
compute sizes of all connected components.
sort and display.
"""

from timeit import timeit
from sys import argv

from geo.point import Point


def load_instance(filename):
    """
    loads .pts file.
    returns distance limit and points.
    """
    with open(filename, "r") as instance_file:
        lines = iter(instance_file)
        distance = float(next(lines))
        points = [Point([float(f) for f in l.split(",")]) for l in lines]

    return distance, points


def insertion(tab, elem):
    """
    insere un element dans une liste triee dans l'ordre decroissant
    """
    i = 0
    if tab:
        while i < len(tab) and elem < tab[i]:
            i += 1
    tab.insert(i, elem)


def print_components_sizes(distance, points):
    """
    affichage des tailles triees de chaque composante
    """
    n_points = len(points)
    points.sort()
    components_sizes = []
    processed = set()
    stack = []

    def neighbors(i, j_min):
        point = points[i]
        point_x = point.coordinates[0]

        j = i + 1
        while j < n_points and points[j].coordinates[0] - point_x <= distance:
            if j not in processed:
                if point.distance_to(points[j]) <= distance:
                    yield j
            j += 1

        j = i - 1
        while j > j_min and point_x - points[j].coordinates[0] <= distance:
            if j not in processed:
                if point.distance_to(points[j]) <= distance:
                    yield j
            j -= 1

    for index in range(n_points):
        if index not in processed:
            processed.add(index)
            size = 1
            stack.append(index)
            while stack:
                i = stack.pop()
                for neighbor in neighbors(i, index):
                    processed.add(neighbor)
                    size += 1
                    stack.append(neighbor)
            insertion(components_sizes, size)

    print(components_sizes)


def main():
    """
    ne pas modifier: on charge une instance et on affiche les tailles
    """
    for instance in argv[1:]:
        distance, points = load_instance(instance)
        print_components_sizes(distance, points)


main()
