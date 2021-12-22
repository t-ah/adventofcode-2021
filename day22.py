import re


def main():
    run("test.txt", Cube([-50, 50, -50, 50, -50, 50]))
    run("day22.txt", Cube([-50, 50, -50, 50, -50, 50]))
    run("test.txt")
    run("day22.txt")


def run(file_name, start_cube=None):
    lines = read_input(file_name)
    cubes = [(line.startswith("on"), Cube(list(map(int, re.findall(r"-?\d+", line))))) for line in lines]
    
    if start_cube == None:
        x_min = find(min, 0, cubes)
        x_max = find(max, 1, cubes)
        y_min = find(min, 2, cubes)
        y_max = find(max, 3, cubes)
        z_min = find(min, 4, cubes)
        z_max = find(max, 5, cubes)
        start_cube = Cube([x_min, x_max, y_min, y_max, z_min, z_max])
    
    for activate, cube in cubes:
        start_cube.add_cube(start_cube.intersection(cube), activate)
    print(start_cube.active_volume())


def find(fct, index, cubes):
    return fct(cubes, key=lambda k: k[1].points[index])[1].points[index]


class Cube:
    def __init__(self, points):
        self.points = points
        self.cuts = []
        self.cubes = []

    def add_cube(self, cube, activate):
        if not cube:
            return
        for on_cube in self.cubes:
            on_cube.cut_out(cube)
        if activate:
            self.cubes.append(cube)

    def cut_out(self, cube):
        intersection_cube = self.intersection(cube)
        if intersection_cube:
            self.cuts.append(intersection_cube)

    def intersection(self, cube):
        x_overlap = self.coordinate_overlap(cube, 0, 1)
        if not x_overlap:
            return None
        y_overlap = self.coordinate_overlap(cube, 2, 3)
        if not y_overlap:
            return None
        z_overlap = self.coordinate_overlap(cube, 4, 5)
        if not z_overlap:
            return None
        return Cube(x_overlap + y_overlap + z_overlap)

    def coordinate_overlap(self, cube, i1, i2):
        interval = [max(self.points[i1], cube.points[i1]), min(self.points[i2], cube.points[i2])]
        if interval[0] > interval[1]:
            return None
        return interval

    def size(self):
        return self.distance(0) * self.distance(2) * self.distance(4)

    def distance(self, axis):
        return 1 + abs(self.points[axis + 1] - self.points[axis])

    def volume(self):
        return self.size() - self.cubeset_volume(self.cuts)

    def cubeset_volume(self, cubes):
        if not cubes:
            return 0
        volume = cubes[0].size() + self.cubeset_volume(cubes[1:])
        intersections = [x for x in [cubes[0].intersection(cube) for cube in cubes[1:]] if x != None]
        return volume - self.cubeset_volume(intersections)

    def active_volume(self):
        return sum([c.volume() for c in self.cubes])


def read_input(file_name):
    with open(file_name, "r") as f:
        return [x.strip() for x in f.readlines()]


if __name__ == "__main__":
    main()