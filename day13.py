def main():
    text = read_input("day13.txt")
    numbers = [tuple(map(int, x.split(","))) for x in text[0].split("\n")]
    raw_foldings = [x.split(" ")[-1].split("=") for x in text[1].split("\n")]
    foldings = [(x[0], int(x[1])) for x in raw_foldings]
    dots = set(numbers)

    for folding in foldings[:1]:
        dots = fold(dots, *folding)
    print(len(dots))

    for folding in foldings[1:]:
        dots = fold(dots, *folding)
    print_grid(dots)


def fold(dots, axis, fold_p):
    new_dots = set()
    for dot in dots:
        dot_p = dot[0] if axis == "x" else dot[1]
        if dot_p < fold_p:
            new_dots.add(dot)
        else:
            offset = dot_p - fold_p
            if axis == "x":
                new_dots.add((fold_p - offset, dot[1]))
            else:
                new_dots.add((dot[0], fold_p - offset))
    return new_dots


def print_grid(dots):
    max_x = max(dots, key=lambda x: x[0])[0]
    max_y = max(dots, key=lambda x: x[1])[1]
    for y in range(max_y + 1):
        line = ""
        for x in range(max_x + 1):
            line += "%" if (x,y) in dots else " "
        print(line)


def read_input(file_name):
    with open(file_name, "r") as f:
        return f.read().split("\n\n")


if __name__ == "__main__":
    main()