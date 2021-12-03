def main():
    lines = read_input("day03.txt")
    length = len(lines[0])

    gamma = "".join(find_common(lines, i, True) for i in range(length))
    epsilon = "".join(["1" if c == "0" else "0" for c in gamma])

    print(bitstr_to_int(epsilon) * bitstr_to_int(gamma))
    print(find_rating(lines, most_common=True) * find_rating(lines, most_common=False))


def find_rating(lines, most_common=True):
    line_set = set(lines)
    for i in range(len(lines[0])):
        filter_out(line_set, i, most_common)
        if len(line_set) == 1:
            return bitstr_to_int(list(line_set)[0])
    print("No number found. That's weird.")


def filter_out(numbers, index, most_common):
    crit = find_common(numbers, index, most_common)
    for n in numbers.copy():
        if n[index] != crit:
            numbers.remove(n)


def find_common(numbers, index, most_common):
    count = 0
    for n in numbers:
        if n[index] == "1":
            count += 1
    if count >= len(numbers)/2:
        return "1" if most_common else "0"
    if count < len(numbers)/2:
        return "0" if most_common else "1"


def bitstr_to_int(s):
    return int(s, 2)


def read_input(file_name):
    with open(file_name, "r") as f:
        return [x.strip() for x in f.readlines()]


if __name__ == "__main__":
    main()