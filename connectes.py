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


def near(point, other, distance):
    """
    renvoie True si les points sont proches en abscisse
    """
    x_1 = point.coordinates[0]
    x_2 = other.coordinates[0]
    return abs(x_2 - x_1) <= distance


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

    for i in range(n_points):
        if i not in processed:
            processed.add(i)
            components_sizes.append(1)
            stack.append(i)
            while stack:
                index = stack.pop()
                for neighbor in neighbors(index, i):
                    processed.add(neighbor)
                    components_sizes[-1] += 1
                    stack.append(neighbor)

    components_sizes.sort(reverse=True)
    print(components_sizes)


def main():
    """
    ne pas modifier: on charge une instance et on affiche les tailles
    """
    for instance in argv[1:]:
        distance, points = load_instance(instance)
        print_components_sizes(distance, points)


main()
