#!/usr/bin/env python3
"""
compute sizes of all connected components.
sort and display.
"""

from timeit import timeit
from sys import argv, setrecursionlimit

class Point:
    def __init__(self, coordinates, processed=False):
        """
        build new point using an array of coordinates.
        """
        self.coordinates = coordinates
        self.processed = processed

    def distance_to(self, other):
        """
        euclidean distance between two points.
        """
        if self < other:
            return other.distance_to(self)  # we are now a symmetric function

        total = 0
        for c_1, c_2 in zip(self.coordinates, other.coordinates):
            diff = c_1 - c_2
            total += diff * diff

        return total**(1/2)

    def __lt__(self, other):
        """
        lexicographical comparison
        """
        return self.coordinates < other.coordinates


def partition(points, axis, g, d):
    pivot = points[g]
    m = g
    for i in range(g+1, d):
        if points[i].coordinates[axis] < pivot.coordinates[axis]:
            m += 1
            if i > m:
                points[i], points[m] = points[m], points[i]
    if m > g:
        points[m], points[g] = points[g], points[m]
    return m


def mediane(points, axis):
    k = len(points) // 2

    def aux(g, d):
        m = partition(points, axis, g, d)
        if m == k:
            return points[m]
        elif m < k:
            return aux(m+1, d)
        else:
            return aux(g, m)

    return aux(0, len(points))


class Node:
    def __init__(self, point, axis, left=None, right=None):
        self.point = point
        self.axis = axis
        self.left = left
        self.right = right


class Tree:
    def __init__(self, points):
        self.root = self.construct(points)

    def construct(self, points, depth=0):
        if not points:
            return None

        axis = depth % 2
        median = mediane(points, axis)
        m = len(points) // 2

        return Node(median, axis, self.construct(points[:m], depth+1), self.construct(points[m+1:], depth+1))


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
