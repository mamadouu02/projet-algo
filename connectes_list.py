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


def print_components_sizes(distance, points):
    """
    affichage des tailles triees de chaque composante
    """
    n_points = len(points)
    points.sort()
    components_sizes = []

    def component_size(i, j):
        """
        calcul de la taille d'une composante connexe
        """
        if j_min < j < n_points:
            if not points[j].processed:
                point, other = points[i], points[j]
                delta = abs(other.coordinates[0] - point.coordinates[0])
                if delta <= distance:
                    if point.distance_to(other) <= distance:
                        points[j].processed = True
                        components_sizes[-1] += 1
                        component_size(j, j+1)
                        component_size(j, j-1)
                    if i < j:
                        component_size(i, j+1)
                    else:
                        component_size(i, j-1)
            else:
                if i < j:
                    component_size(i, j+1)
                else:
                    component_size(i, j-1)

    for i in range(n_points):
        if not points[i].processed:
            points[i].processed = True
            components_sizes.append(1)
            j_min = i
            component_size(i, i+1)

    components_sizes.sort(reverse=True)
    print(components_sizes)


def main():
    """
    ne pas modifier: on charge une instance et on affiche les tailles
    """
    for instance in argv[1:]:
        distance, points = load_instance(instance)
        print_components_sizes(distance, points)


setrecursionlimit(1000000000)
main()
