from collections import defaultdict
from queue import Queue
from functools import reduce


def main():
    h = read_input("day09.txt")
    lenX, lenY = len(h), len(h[0])
    grid = defaultdict(lambda : 10)
    for x in range(lenX):
        for y in range(lenY):
            grid[(x,y)] = h[x][y]
    lp = get_low_points(grid, lenX, lenY)
    print(sum([grid[p] for p in lp]) + len(lp))

    basin_sizes = []
    for p in lp:
        basin = flood(grid, p)
        basin_sizes.append(len(basin))
    basin_sizes.sort()
    print(reduce(lambda x, y: x * y, basin_sizes[-3:], 1))


def get_low_points(grid, lenX, lenY):
    res = []
    for x in range(lenX):
        for y in range(lenY):
            height = grid[(x, y)]
            low = True
            for neighbour in neighbours(x, y):
                if grid[neighbour] <= height:
                    low = False
                    break
            if low:
                res.append((x, y))
    return res


def flood(grid, origin):
    queue = Queue()
    queue.put(origin)
    expanded = set()
    while not queue.empty():
        point = queue.get()
        if point in expanded:
            continue
        expanded.add(point)
        for n in neighbours(*point):
            if grid[n] >= 9 or n in expanded:
                continue
            queue.put(n)
    return expanded


def neighbours(x, y):
    return [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]


def read_input(file_name):
    with open(file_name, "r") as f:
        return [[int(s) for s in list(x.strip())] for x in f.readlines()]


if __name__ == "__main__":
    main()