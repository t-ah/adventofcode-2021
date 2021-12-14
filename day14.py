from collections import defaultdict, Counter
import math


def main():
    lines = read_input("day14.txt")
    template = lines[0]
    rules = [x.split(" -> ") for x in lines[2:]]
    pairs = [template[i:i + 2] for i in range(len(template) - 1)]
    counts = defaultdict(int)
    for p in pairs:
        counts[p] += 1

    for _ in range(10):
        step(counts, rules)
    evaluate(counts)

    for _ in range(30):
        step(counts, rules)
    evaluate(counts)


def step(counts, rules):
    new_pairs = defaultdict(int)
    for rule in rules:
        count = counts[rule[0]]
        new_pairs[rule[0][0] + rule[1]] += count
        new_pairs[rule[1] + rule[0][1]] += count
    for rule in rules:
        counts[rule[0]] = 0
    for pair in new_pairs:
        counts[pair] = new_pairs[pair]


def evaluate(counts):
    letter_count = Counter()
    for pair, count in counts.items():
        for letter in pair:
            letter_count[letter] += count
    for key in letter_count:
        letter_count[key] = math.ceil(letter_count[key] / 2)
    result = letter_count.most_common()
    print(result[0][1] - result[-1][1])


def read_input(file_name):
    with open(file_name, "r") as f:
        return [x.strip() for x in f.readlines()]


if __name__ == "__main__":
    main()