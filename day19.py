from collections import Counter
from queue import deque


def main():
    scans = read_input("day19.txt")
    fixed_scans = scans[:1]
    unfixed_scans = deque(scans[1:])
    scanner_offsets = []
    
    while unfixed_scans:
        unfixed_scan = unfixed_scans.popleft()
        fixed_scan, offsets = compare_scans(unfixed_scan, fixed_scans)
        if fixed_scan:
            fixed_scans.append(fixed_scan)
            scanner_offsets.append(offsets)
        else:
            unfixed_scans.append(unfixed_scan)
    beacons = set()
    for scan in fixed_scans:
        for pos in scan:
            beacons.add(tuple(pos))
    print(len(beacons))
    
    max_distance = 0
    for i in range(len(scanner_offsets)):
        for j in range(i + 1, len(scanner_offsets)):
            pos1, pos2 = scanner_offsets[i], scanner_offsets[j]
            distance = sum([abs(pos1[i] - pos2[i]) for i in range(3)])
            max_distance = max(distance, max_distance)
    print(max_distance)


def compare_scans(unfixed_scan, fixed_scans):
    for rotated_scan in generate_rotations(unfixed_scan):
        for fixed_scan in fixed_scans:
            counter = Counter()
            for pos1 in fixed_scan:
                for pos2 in rotated_scan:
                    counter[diff(pos1, pos2)] += 1
            offsets, overlap = counter.most_common()[0]
            if overlap >= 12:
                # return [[pos[0] + offsets[0], pos[1] + offsets[1], pos[2] + offsets[2]] for pos in rotated_scan], offsets
                return [[pos[i] + offsets[i]] for pos in rotated_scan for i in range(3)], offsets
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