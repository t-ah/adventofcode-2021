def main():
    positions = read_input("day07.txt")
    positions.sort()
    print(find_minimum(positions, False))
    print(find_minimum(positions, True))


def find_minimum(positions, correct):
    fuel = [calculate_fuel(positions, i, correct) for i in range(positions[0], positions[-1] + 1)]
    return min(fuel)


def calculate_fuel(positions, i, correct):
    fuel = 0
    for p in positions:
        distance = abs(p - i)
        fuel += distance * (distance + 1) if correct else distance
    return fuel // 2 if correct else fuel


def read_input(file_name):
    with open(file_name, "r") as f:
        return [int(n) for n in f.read().split(",")]


if __name__ == "__main__":
    main()