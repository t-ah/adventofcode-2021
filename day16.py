from queue import deque
from functools import reduce


def main():
    hex = read_input("day16.txt")
    bits = ""
    for c in hex:
        res = "{0:04b}".format(int(c, 16))
        bits += res
    q = deque(bits)
    p = parse_packet(q)
    print("versions", p.sum_versions())
    print("value", p.evaluate())


class Packet:
    def __init__(self, version, type, content):
        self.version = version
        self.type = type
        self.content = content

    def evaluate(self):
        if self.type == 4:
            return self.content
        else:
            values = [sub_p.evaluate() for sub_p in self.content]
            if self.type == 0:
                return sum(values)
            elif self.type == 1:
                return reduce(lambda x, y: x * y, values)
            elif self.type == 2:
                return min(values)
            elif self.type == 3:
                return max(values)
            elif self.type == 5:
                return 1 if values[0] > values[1] else 0
            elif self.type == 6:
                return 1 if values[0] < values[1] else 0
            elif self.type == 7:
                return 1 if values[0] == values[1] else 0

    def sum_versions(self):
        v = self.version
        if self.type != 4:
            for sub_p in self.content:
                v += sub_p.sum_versions()
        return v


def parse_packet(q):
    version = bits_to_int(get_bits(q, 3))
    type_id = bits_to_int(get_bits(q, 3))
    if type_id == 4:
        number = parse_number(q)
        return Packet(version, type_id, number)
    else:
        lt_ID = q.popleft()
        sub_packets = []
        if lt_ID == "0":
            next_packet_bits = bits_to_int(get_bits(q, 15))
            target_length = len(q) - next_packet_bits
            while len(q) != target_length:
                sub_packets.append(parse_packet(q))
        else:
            length = bits_to_int(get_bits(q, 11))
            for _ in range(length):
                sub_packets.append(parse_packet(q))
        return Packet(version, type_id, sub_packets)


def parse_number(q):
    read_bits = 6
    number = []
    while True:
        read_bits += 5
        frame = get_bits(q, 5)
        number += frame[1:]
        if frame[0] == "0":
            break
    return bits_to_int(number)


def get_bits(q, n):
    return [q.popleft() for _ in range(n)]


def bits_to_int(bit_list):
    return int("".join(bit_list), 2)


def read_input(file_name):
    with open(file_name, "r") as f:
        return f.read()


if __name__ == "__main__":
    main()