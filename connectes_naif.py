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


def explore_connexe_comp(dist, points, visited, first):
    size, pile = 0, [first]

    # Tant que la pile des voisins du sommet traité est non vide faire :
    while pile:
        indice_pts = pile.pop()

        # Rend le point courrant traité
        visited[indice_pts] = True
        size += 1

        # Recherche de voisins 
        for i, point in enumerate(points):
            if not visited[i] and i not in pile:
                    if points[indice_pts].distance_to(points[i]) <= dist:
                        pile.append(i)

    return size


def print_components_sizes(dist, points):
    n_pts, components_sizes, grid = len(points), [], {}
    visited = [False] * n_pts

    # Tant que les sommets n'ont pas tous été traités, appeler la fonction
    for k in range(n_pts):
        if not(visited[k]):
            size = explore_connexe_comp(dist, points, visited, k)
            components_sizes += [size]

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
