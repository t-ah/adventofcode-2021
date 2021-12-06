import re
from collections import defaultdict


def main():
    lines = read_input("day05.txt")
    pattern = re.compile("([0-9]+),([0-9]+) -> ([0-9]+),([0-9]+)")
    coordinates = [list(map(int, l)) for l in [re.search(pattern, line).groups() for line in lines]]
    print(count_overlap(coordinates, 2, False))
    print(count_overlap(coordinates, 2, True))


def count_overlap(coordinates, threshold, diagonals=True):
    counts = defaultdict(int)
    for c in coordinates:
        if c[0] == c[2] or c[1] == c[3]:
            count_line(c, counts)
        elif diagonals:
            count_diagonal(c, counts)
    return sum(i >= threshold for i in counts.values())


def count_line(c, counts):
    for x in sequence(c[0], c[2]):
        for y in sequence(c[1], c[3]):
            counts[(x,y)] += 1


def count_diagonal(c, counts):
    deltaY = 1 if c[3] > c[1] else -1
    y = c[1]
    for x in sequence(c[0], c[2]):
        counts[(x, y)] += 1
        y += deltaY


def sequence(v1, v2):
    if v1 < v2:
        return range(v1, v2 + 1)
    else:
        return range(v1, v2 - 1, -1)


def read_input(file_name):
    with open(file_name, "r") as f:
        return [x.strip() for x in f.readlines()]


if __name__ == "__main__":
    main()