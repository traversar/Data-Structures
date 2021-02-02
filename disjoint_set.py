class Node:
    def __init__(self, data):
        self.data = data


def create(x):
    x.rank = 0
    x.parent = x


def union(x, y):
    x, y = find(x), find(y)
    if x.rank > y.rank:
        y.parent = x
    else:
        x.parent = y
        if x.rank == y.rank:
            y.rank += 1


def find(x):
    if x != x.parent:
        x.parent = find(x.parent)
    return x.parent
