"""
2-d tree.
"""

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
