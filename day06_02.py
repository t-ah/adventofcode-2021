def main():
    numbers = read_input("day06.txt")
    counts = [numbers.count(i) for i in range(9)]
    print(simulate(counts.copy(), 80))
    print(simulate(counts.copy(), 256))


def simulate(counts, days):
    for _ in range(days):
        counts = counts[1:] + counts[:1]
        counts[6] += counts[-1]
    return sum(counts)


def read_input(file_name):
    with open(file_name, "r") as f:
        return [int(n) for n in f.read().split(",")]


if __name__ == "__main__":
    main()