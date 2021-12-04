def main():
    lines = read_input("day03.txt")
    length = len(lines[0])

    gamma = "".join(find_common(lines, i, True) for i in range(length))
    epsilon = "".join(["1" if c == "0" else "0" for c in gamma])

    print(bitstr_to_int(epsilon) * bitstr_to_int(gamma))
    print(find_rating(lines, most_common=True) * find_rating(lines, most_common=False))


def find_rating(lines, most_common=True):
    remaining_lines = list(lines)
    for i in range(len(lines[0])):
        crit = find_common(remaining_lines, i, most_common)
        remaining_lines = list(filter(lambda n: n[i] != crit, remaining_lines))
        if len(remaining_lines) == 1:
            return bitstr_to_int(remaining_lines[0])
    print("No number found. That's weird.")


def find_common(numbers, index, most_common):
    ones_count = 0
    for n in numbers:
        if n[index] == "1":
            ones_count += 1
    if ones_count >= len(numbers)/2:
        return "1" if most_common else "0"
    else:
        return "0" if most_common else "1"


def bitstr_to_int(s):
    return int(s, 2)


def read_input(file_name):
    with open(file_name, "r") as f:
        return [x.strip() for x in f.readlines()]


if __name__ == "__main__":
    main()