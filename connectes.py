#!/usr/bin/env python3
"""
compute sizes of all connected components.
sort and display.
"""

from timeit import timeit
from sys import argv, setrecursionlimit

from geo.point import Point


class Node:
    def __init__(self, index, axis, left=None, right=None):
        self.index = index
        self.axis = axis
        self.left = left
        self.right = right


class Tree:
    def __init__(self, points):
        indexes = list(range(len(points)))
        self.points = points
        self.root = self.construct(indexes)

    def construct(self, indexes, depth=0):
        if not indexes:
            return None

        axis = depth % 2
        indexes.sort(key=lambda i : self.points[i].coordinates[axis])
        m = len(indexes) // 2
        median = indexes[m]

        return Node(median, axis, self.construct(indexes[:m], depth+1), self.construct(indexes[m+1:], depth+1))


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
    n_points = len(points)
    processed = [False] * n_points

    def search(node, i):
        if node is not None:
            j = node.index
            axis = node.axis
            point, other = points[i], points[j]
            delta = other.coordinates[axis] - point.coordinates[axis]
            if abs(delta) <= distance:
                if not processed[j] and point.distance_to(other) <= distance:
                    processed[j] = True
                    components_sizes[-1] += 1
                    search(tree.root, j)
                search(node.left, i)
                search(node.right, i)
            elif delta > 0:
                search(node.left, i)
            else:
                search(node.right, i)

    for i in range(n_points):
        if not processed[i]:
            processed[i] = True
            components_sizes.append(1)
            search(tree.root, i)

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
