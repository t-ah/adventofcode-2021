from collections import defaultdict


def main():
    lines = read_input("day20.txt")
    algorithm = lines[0]
    image = Image(lines[2:])

    for _ in range(2):
        image.enhance(algorithm)
    print(image.count_light())

    for _ in range(48):
        image.enhance(algorithm)
    print(image.count_light())


class Image:
    def __init__(self, lines):
        self.infinite = "."
        self.offsets = (-1, 0, 1)
        self.content = self.empty_content()
        self.x_bounds = [0, len(lines[0])]
        self.y_bounds = [0, len(lines)]
        for y, line in enumerate(lines):
            for x, ch in enumerate(line):
                self.content[(x, y)] = "1" if ch == "#" else "0"

    def enhance(self, algorithm):
        self.infinite = algorithm[0] if self.infinite == "." else algorithm[-1]
        enhanced = self.empty_content()
        self.x_bounds[0] -= 1
        self.x_bounds[1] += 1
        self.y_bounds[0] -= 1
        self.y_bounds[1] += 1
        for y in range(*self.y_bounds):
            for x in range(*self.x_bounds):
                bitstr = ""
                for dy in self.offsets:
                    for dx in self.offsets:
                        bitstr += self.content[(x + dx, y + dy)]
                index = int(bitstr, 2)
                enhanced[(x, y)] = "1" if algorithm[index] == "#" else "0"
        self.content = enhanced

    def empty_content(self):
        s = "1" if self.infinite == "#" else "0"
        return defaultdict(lambda: s)

    def count_light(self):
        return list(self.content.values()).count("1")

    def print(self):
        for y in range(*self.y_bounds):
            line = ""
            for x in range(*self.x_bounds):
                line += "#" if self.content[(x, y)] == "1" else "."
            print(line)


def read_input(file_name):
    with open(file_name, "r") as f:
        return [x.strip() for x in f.readlines()]


if __name__ == "__main__":
    main()