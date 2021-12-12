from collections import defaultdict


paths = []
connections = defaultdict(lambda : set())


def main():
    lines = read_input("day12.txt")
    for n1, n2 in lines:
        connections[n1].add(n2)
        connections[n2].add(n1)
    path = ["start"]
    advance(path)
    print(len(paths))

    paths.clear()
    path = ["start"]
    advanceTwice(path, False)
    print(len(paths))


def advance(path):
    current_node = path[-1]
    for node in connections[current_node]:
        if node[0].isupper() or node not in path:
            new_path = path + [node]
            if node == "end":
                paths.append(new_path)
            else:
                advance(new_path)


def advanceTwice(path, visitedTwice):
    current_node = path[-1]
    for node in connections[current_node]:
        if node == "start":
            continue
        if node[0].isupper() or node not in path or not visitedTwice:
            new_path = path + [node]
            if node == "end":
                paths.append(new_path)
            else:
                twice = visitedTwice or (node.islower() and node in path)
                advanceTwice(new_path, twice)


def read_input(file_name):
    with open(file_name, "r") as f:
        return [x.strip().split("-") for x in f.readlines()]


if __name__ == "__main__":
    main()