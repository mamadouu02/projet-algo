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

def explore_connexe_comp(dist,points,visited,grid,first,square_neighbor):
    """Calcule la taille d'une composante connexe"""
    size,pile = 0,set([first])
    # Tant que la pile des voisins du sommet traité est non nul faire:
    while len(pile) != 0 :
        indice_pts = pile.pop()
        current_pts = points[indice_pts]
        approx_pts = int(current_pts.coordinates[0]/dist),int(current_pts.coordinates[1]/dist)
        
        # Rend le point courrent traité
        visited[indice_pts] = True
        grid[approx_pts].pop(indice_pts)
        size += 1

        # Recherche optimisée de possibles vosins 
        for coord in square_neighbor:
            key = (approx_pts[0] + coord[0],approx_pts[1] + coord[1])
            for index_possible_neighbor in grid.get(key,{}):
                if not visited[index_possible_neighbor]:
                    if points[indice_pts].distance_to(grid[key][index_possible_neighbor]) <= dist :
                        pile.add(index_possible_neighbor)

    return size

def print_components_sizes(dist, points):
    """
    affichage des tailles triees de chaque composante
    """
    n_pts,components_sizes,grid = len(points),[],{}
    visited = [False for _ in range(n_pts)]
    square_neighbor = [(-1, -1), (0, -1), (1, -1), (-1, 0), (0, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]

    # On ordonne les points par paquets qui appartiennent au même carré de coté dist 
    # grâce à l'approximation à l'entier le plus proche + structure de dictionnaire
    for k in range(n_pts):
        pts_k = points[k]
        approx_pts = int(pts_k.coordinates[0]/dist),int(pts_k.coordinates[1]/dist)
        square = grid.get(approx_pts, {})
        square[k] = pts_k
        grid[approx_pts] = square


    # Tant que les sommets n'ont pas tous été traités, appliquer la fonction
    for k in range(n_pts):
        if not(visited[k]):
            size = explore_connexe_comp(dist,points,visited,grid,k,square_neighbor)
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