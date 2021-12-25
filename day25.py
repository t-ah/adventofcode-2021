def main():
    lines = read_input("day25.txt")
    east, south = set(), set()
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if c == ">":
                east.add((x, y))
            elif c == "v":
                south.add((x, y))
    lenX, lenY = len(lines[0]), len(lines)

    step_count = 0
    moved = True
    while moved:
        step_count += 1
        east, south, moved = step(east, south, lenX, lenY)
    print(step_count)


def step(east, south, lenX, lenY):
    new_east, new_south = set(), set()
    moved = False
    for c in east:
        c_new = ((c[0] + 1) % lenX, c[1])
        if c_new not in east and c_new not in south:
            new_east.add(c_new)
            moved = True
        else:
            new_east.add(c)
    for c in south:
        c_new = (c[0], (c[1] + 1) % lenY)
        if c_new not in new_east and c_new not in south:
            new_south.add(c_new)
            moved = True
        else:
            new_south.add(c)
    return new_east, new_south, moved


def read_input(file_name):
    with open(file_name, "r") as f:
        return [x.strip() for x in f.readlines()]


if __name__ == "__main__":
    main()