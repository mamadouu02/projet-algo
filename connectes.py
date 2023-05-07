#!/usr/bin/env python3
"""
compute sizes of all connected components.
sort and display.
"""

from timeit import timeit
from sys import argv, setrecursionlimit

from geo.point import Point
from geo.tree import Tree


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
    tree = Tree(points)
    components_sizes = []

    def search(node, point):
        """
        calcul de la taille d'une composante connexe
        """
        if node is not None:
            other = node.point
            axis = node.axis
            delta = other.coordinates[axis] - point.coordinates[axis]
            if abs(delta) <= distance:
                if not other.processed and point.distance_to(other) <= distance:
                    other.processed = True
                    components_sizes[-1] += 1
                    search(tree.root, other)
                search(node.left, point)
                search(node.right, point)
            elif delta > 0:
                search(node.left, point)
            else:
                search(node.right, point)

    for point in points:
        if not point.processed:
            point.processed = True
            components_sizes.append(1)
            search(tree.root, point)

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
