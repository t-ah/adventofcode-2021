def main():
    lines = read_input("day08.txt")
    entries = [l.split(" ") for l in lines]
    count = 0
    output_sum = 0
    for entry in entries:
        codes = [set(x) for x in entry[:10] + entry[11:]]
        result = decode(codes)
        outputs = result[-4:]
        for i in [1, 4, 7, 8]:
            count += outputs.count(i)
        output_sum += 1000 * outputs[0] + 100 * outputs[1] + 10 * outputs[2] + outputs[3]
    print(count)
    print(output_sum)


def decode(codes):
    lookup = {"abcdefg" : 8}
    segments_cf = filterLen(codes, 2)[0]
    lookup[set_to_key(segments_cf)] = 1
    segment_a = filterLen(codes, 3)[0] - segments_cf
    lookup[set_to_key(segments_cf.union(segment_a))] = 7
    segments_bd = filterLen(codes, 4)[0] - segments_cf
    lookup[set_to_key(segments_cf.union(segments_bd))] = 4
    codes235 = filterLen(codes, 5)
    for segments in codes235:
        if segments_cf.issubset(segments):
            lookup[set_to_key(segments)] = 3
        elif segments_bd.issubset(segments):
            lookup[set_to_key(segments)] = 5
        else:
            lookup[set_to_key(segments)] = 2
    codes069 = filterLen(codes, 6)
    for segments in codes069:
        if not segments_cf.issubset(segments):
            lookup[set_to_key(segments)] = 6
        elif segments_bd.issubset(segments):
            lookup[set_to_key(segments)] = 9
        else:
            lookup[set_to_key(segments)] = 0
    return [lookup[set_to_key(x)] for x in codes]


def set_to_key(key_set):
    key_list = list(key_set)
    key_list.sort()
    return "".join(key_list)


def filterLen(codes, length):
    return [x for x in codes if len(x) == length]


def read_input(file_name):
    with open(file_name, "r") as f:
        return [x.strip() for x in f.readlines()]


if __name__ == "__main__":
    main()