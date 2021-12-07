from functools import cache


def main():
    numbers = read_input("day06.txt")
    print(get_swarm(numbers, 80))
    print(get_swarm(numbers, 256))


def get_swarm(numbers, days):
    return sum(get_fish(n, days) for n in numbers)


@cache
def get_fish(n, days):
    if days == 0:
        return 1
    if n == 0:
        return get_fish(6, days - 1) + get_fish(8, days - 1)
    return get_fish(n - 1, days - 1)


def read_input(file_name):
    with open(file_name, "r") as f:
        return [int(n) for n in f.read().split(",")]


if __name__ == "__main__":
    main()