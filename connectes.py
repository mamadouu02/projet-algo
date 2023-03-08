#!/usr/bin/env python3
"""
compute sizes of all connected components.
sort and display.
"""

from timeit import timeit
from sys import argv, setrecursionlimit

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
    processed = [False] * n_points
    components_sizes = []
    setrecursionlimit(1000000)

    def component_size(i, j, j_min):
        """
        incremente la taille de la composante si les points sont proches
        """
        if j_min < j < n_points:
            if not processed[j]:
                point, other = points[i], points[j]
                if near(point, other, distance):
                    if point.distance_to(other) <= distance:
                        processed[j] = True
                        components_sizes[-1] += 1
                        component_size(j, j+1, j_min)
                        component_size(j, j-1, j_min)
                    if i < j:
                        component_size(i, j+1, j_min)
                    else:
                        component_size(i, j-1, j_min)
            else:
                if i < j:
                    component_size(i, j+1, j_min)
                else:
                    component_size(i, j-1, j_min)

    for i in range(n_points):
        if not processed[i]:
            processed[i] = True
            components_sizes.append(1)
            component_size(i, i+1, i)
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
