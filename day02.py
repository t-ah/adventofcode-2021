def main():
    cmds = read_input("day02.txt")
    
    x, y = 0, 0
    for cmd in cmds:
        if cmd[0] == "forward":
            x += cmd[1]
        elif cmd[0] == "down":
            y += cmd[1]
        elif cmd[0] == "up":
            y -= cmd[1]
    print(x, y, x * y)

    x, y, aim = 0, 0, 0
    for cmd in cmds:
        if cmd[0] == "forward":
            x += cmd[1]
            y += aim * cmd[1]
        elif cmd[0] == "down":
            aim += cmd[1]
        elif cmd[0] == "up":
            aim -= cmd[1]
    print(x, y, x * y)


def read_input(file_name):
    with open(file_name, "r") as f:
        return [(d, int(n)) for d, n in [x.strip().split(" ") for x in f.readlines()]]


if __name__ == "__main__":
    main()