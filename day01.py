def main():
    depths = read_input("day01.txt")
    print(count_increments(depths, window_size=1))
    print(count_increments(depths, window_size=3))


def read_input(file_name):
    with open(file_name, "r") as f:
        return [int(x) for x in f.readlines()]


def count_increments(values, window_size=2):
    count = 0
    prev = sum(values[:window_size])
    for i in range(1, len(values) - window_size + 1):
        s = sum(values[i:i + window_size])
        if s > prev:
            count += 1
        prev = s
    return count


if __name__ == "__main__":
    main()