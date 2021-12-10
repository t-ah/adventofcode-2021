from queue import LifoQueue


score_table_corrupt = {")": 3, "]": 57, "}": 1197, ">": 25137}
score_table_incomplete = {"(": 1, "[": 2, "{": 3, "<": 4}
matching_open = {")": "(", "]": "[", "}": "{", ">": "<"}


def main():
    lines = read_input("day10.txt")
    corrupt_score = 0
    incomplete_scores = []
    for line in lines:
        corrupt, line_score = check_line(line)
        if corrupt:
            corrupt_score += line_score
        else:
            incomplete_scores.append(line_score)
    print(corrupt_score)
    incomplete_scores.sort()
    print(incomplete_scores[len(incomplete_scores) // 2])


def check_line(line):
    stack = LifoQueue()
    score = 0
    for c in line:
        if c in matching_open:
            if stack.empty():
                return 0
            actual_open = stack.get()
            c_open = matching_open[c]
            if c_open != actual_open and score == 0:
                score = score_table_corrupt[c]
        else:
            stack.put(c)
    if score != 0:
        return True, score
    while not stack.empty():
        score = 5 * score + score_table_incomplete[stack.get()]
    return False, score


def read_input(file_name):
    with open(file_name, "r") as f:
        return [x.strip() for x in f.readlines()]


if __name__ == "__main__":
    main()