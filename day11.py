from queue import Queue


def main():
    lines = read_input("day11.txt")
    numbers = [list(map(int, list(x))) for x in lines]
    grid = {}
    for x in range(10):
        for y in range(10):
            grid[(x,y)] = numbers[y][x]

    result = 0
    for _ in range(100):
        result += step(grid)
    print(result)

    step_count = 100
    while True:
        step_count += 1
        flashes = step(grid)
        if flashes == 100:
            break
    print(step_count)


def step(grid):
    to_flash = Queue()
    flashed = set()
    for x in range(10):
        for y in range(10):
            pos = (x, y)
            grid[pos] += 1
            if grid[pos] == 10:
                to_flash.put(pos)
    while not to_flash.empty():
        pos = to_flash.get()
        flashed.add(pos)
        for new_pos in flash(grid, pos):
            to_flash.put(new_pos)
    for f in flashed:
        grid[f] = 0
    return len(flashed)


def flash(grid, pos):
    result = []
    for n in neighbours(pos):
        grid[n] += 1
        if grid[n] == 10:
            result.append(n)
    return result


def neighbours(pos):
    positions = []
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, +1]:
            x, y = pos[0] + dx, pos[1] + dy
            if x >= 0 and x <= 9 and y >= 0 and y <= 9 and not (dx == 0 and dy == 0):
                positions.append((x, y))
    return positions


def read_input(file_name):
    with open(file_name, "r") as f:
        return [x.strip() for x in f.readlines()]


if __name__ == "__main__":
    main()