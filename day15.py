from sys import maxsize


def main():
    grid = read_input("day15.txt")
    lenY, lenX = len(grid), len(grid[0])

    shortest_path = dijkstra(grid, (0, 0), lenX, lenY)
    print(shortest_path[(lenX - 1, lenY - 1)])

    for line in grid:
        shift = line
        for _ in range(1, 5):
            shift = list(map(lambda x: max(1, (x + 1) % 10), shift))
            line += shift
    for l in range(lenY, 5 * lenY):
        original = grid[l - lenY]
        new_line = list(map(lambda x: max(1, (x + 1) % 10), original))
        grid.append(new_line)

    lenY, lenX = len(grid), len(grid[0])
    shortest_path = dijkstra(grid, (0, 0), lenX, lenY)
    print(shortest_path[(lenX - 1, lenY - 1)])


def dijkstra(grid, start, lenX, lenY):
    nodes = [(x, y) for x in range(lenX) for y in range(lenY)]
    unvisited = set()
    unvisited.add(start)
    shortest_path = {node: maxsize for node in nodes}
    shortest_path[start] = 0
    while unvisited:
        min_node = min(unvisited, key=lambda x: shortest_path[x])
        for neighbour in grid_neighbours(*min_node, lenX, lenY):
            v = shortest_path[min_node] + get_value(grid, neighbour)
            if v < shortest_path[neighbour]:
                shortest_path[neighbour] = v
                unvisited.add(neighbour)
        unvisited.remove(min_node)
    return shortest_path


def get_value(grid, node):
    return grid[node[1]][node[0]]


def grid_neighbours(x, y, lenX, lenY):
    positions = []
    if x > 0: positions.append((x - 1, y))
    if x < lenX - 1: positions.append((x + 1, y))
    if y > 0: positions.append((x, y - 1))
    if y < lenY - 1: positions.append((x, y + 1))
    return positions


def read_input(file_name):
    with open(file_name, "r") as f:
        return [list(map(int, list(x.strip()))) for x in f.readlines()]


if __name__ == "__main__":
    main()