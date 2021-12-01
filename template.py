def main():
    sth = read_input("dayX.txt")


def read_input(file_name):
    with open(file_name, "r") as f:
        return [int(x) for x in f.readlines()]


if __name__ == "__main__":
    main()