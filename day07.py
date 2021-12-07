def main():
    positions = read_input("day07.txt")
    positions.sort()
    print("Result:", find_minimum(positions, False, optimised=True))
    print("Result:", find_minimum(positions, True, optimised=True))


def find_minimum(positions, correct, optimised=False):
    if not optimised:
        fuel = [calculate_fuel(positions, i, correct) for i in range(positions[0], positions[-1] + 1)]
        return min(fuel)
    else:
        return search(len(positions) // 2, len(positions) // 2, positions, correct, 0)


def search(index, interval, positions, correct, cnt):
    interval = interval // 2
    v = calculate_fuel(positions, index, correct)
    if interval == 0:
        print("Iterations:", cnt)
        return v
    v_left = calculate_fuel(positions, index - interval, correct)
    if v_left <= v:
        return search(index - interval, interval, positions, correct, cnt + 1)
    v_right = calculate_fuel(positions, index + interval, correct)
    if v_right <= v:
        return search(index + interval, interval, positions, correct, cnt + 1)
    return search(index, interval - 1, positions, correct, cnt + 1)


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