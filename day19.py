from collections import Counter
from queue import deque


def main():
    scans = read_input("day19.txt")
    scans = list(enumerate(scans))
    fixed_scans = scans[:1]
    unfixed_scans = deque(scans[1:])
    scanner_offsets = []
    
    while unfixed_scans:
        unfixed_scan = unfixed_scans.popleft()
        fixed_scan, offsets, relative_to = compare_scans(unfixed_scan, fixed_scans)
        if fixed_scan:
            fixed_scans.append(fixed_scan)
            scanner_offsets.append((fixed_scan[0], relative_to, offsets))
        else:
            unfixed_scans.append(unfixed_scan)
    beacons = set()
    for scan in fixed_scans:
        for pos in scan[1]:
            beacons.add(tuple(pos))
    print(len(beacons))
    
    scanner_positions = {0: (0, 0, 0)}
    for id, relative_to_id, offset in scanner_offsets:
        ref_pos = scanner_positions[relative_to_id]
        ref_pos = (0,0,0) # TODO why do _all_ offsets appear to be relative to (0,0,0)?
        scanner_positions[id] = (ref_pos[0] - offset[0], ref_pos[1] - offset[1], ref_pos[2] - offset[2])
    max_distance = 0
    for i in range(len(scanner_positions)):
        for j in range(i + 1, len(scanner_positions)):
            pos1, pos2 = scanner_positions[i], scanner_positions[j]
            distance = sum([abs(pos1[i] - pos2[i]) for i in range(3)])
            max_distance = max(distance, max_distance)
    print(max_distance)


def compare_scans(unfixed_scan, fixed_scans):
    for rotated_scan in generate_rotations(unfixed_scan[1]):
        for fixed_i, fixed_scan in fixed_scans:
            counter = Counter()
            for pos1 in fixed_scan:
                for pos2 in rotated_scan:
                    counter[diff(pos1, pos2)] += 1
            offsets, overlap = counter.most_common()[0]
            if overlap >= 12:
                return (unfixed_scan[0], [[pos[0] + offsets[0], pos[1] + offsets[1], pos[2] + offsets[2]] for pos in rotated_scan]), offsets, fixed_i
    return None, None, None


def diff(pos1, pos2):
    return tuple([pos1[i] - pos2[i] for i in range(3)])


def get_spacings(scan, index):
    return [scan[i + 1][index] - scan[i][index] for i in range(len(scan) - 1)]


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