from collections import Counter
from queue import deque


def main():
    scans = read_input("day19.txt")
    fixed_scans = scans[:1]
    unfixed_scans = deque(scans[1:])
    positions = []
    
    while unfixed_scans:
        unfixed_scan = unfixed_scans.popleft()
        fixed_scan, position = fix_scan(unfixed_scan, fixed_scans)
        if fixed_scan:
            fixed_scans.append(fixed_scan)
            positions.append(position)
        else:
            unfixed_scans.append(unfixed_scan)

    beacons = set([tuple(pos) for scan in fixed_scans for pos in scan])
    print(len(beacons))

    max_distance = max([manhattan_distance(pos1, pos2) for pos1 in positions for pos2 in positions])
    print(max_distance)

def manhattan_distance(pos1, pos2):
    return sum([abs(pos1[i] - pos2[i]) for i in range(3)])

def fix_scan(unfixed_scan, fixed_scans):
    for rotated_scan in generate_rotations(unfixed_scan):
        for fixed_scan in fixed_scans:
            counter = Counter()
            for pos1 in fixed_scan:
                for pos2 in rotated_scan:
                    counter[diff(pos1, pos2)] += 1
            offsets, overlap = counter.most_common()[0]
            if overlap >= 12:
                return [[pos[i] + offsets[i] for i in range(3)] for pos in rotated_scan], offsets
    return None, None


def diff(pos1, pos2):
    return tuple([pos1[i] - pos2[i] for i in range(3)])


def generate_rotations(positions):
    for _ in range(4):
        positions = rotateY(positions)
        for _ in range(4):
            positions = rotateX(positions)
            yield positions
    positions = rotateZ(positions)
    for _ in range(4):
        positions = rotateX(positions)
        yield positions
    positions = rotateZ(rotateZ(positions))
    for _ in range(4):
        positions = rotateX(positions)
        yield positions


def rotateX(block):
    return [[x, -z, y] for x,y,z in block]


def rotateY(block):
    return [[z, y, -x] for x,y,z in block]


def rotateZ(block):
    return [[-y, x, z] for x,y,z in block]


def read_input(file_name):
    with open(file_name, "r") as f:
        return [list(map(lambda l: list(map(int, l.split(","))), x.split("\n")[1:])) for x in f.read().split("\n\n")]


if __name__ == "__main__":
    main()