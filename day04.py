import re


class Board:
    def __init__(self, lines):
        parts = [re.split(r"\s+", x) for x in lines]
        self.lines = [list(map(lambda n: int(n), part)) for part in parts]
        self.size = len(self.lines)
        self.marked_row = [set() for _ in range(self.size)]
        self.marked_col = [set() for _ in range(self.size)]

    def mark(self, n):
        for row_i, row in enumerate(self.lines):
            if n in row:
                self.marked_row[row_i].add(n)
                col_i = row.index(n)
                self.marked_col[col_i].add(n)
                return self.check_win(row_i, col_i)
        return -1

    def check_win(self, row_i, col_i):
        if len(self.marked_row[row_i]) == self.size or len(self.marked_col[col_i]) == self.size:
            return self.calculate_score()
        return -1

    def calculate_score(self):
        unmarked_sum = 0
        for row_i, row in enumerate(self.lines):
            marked = self.marked_row[row_i]
            for n in row:
                if n not in marked:
                    unmarked_sum += n
        return unmarked_sum


def main():
    lines = read_input("day04.txt")

    boards = []
    for l in range(2, len(lines), 6):
        boards.append(Board(lines[l: l+5]))

    draws = [int(x) for x in lines[0].split(",")]
    scores = []
    for n in draws:
        for board in boards.copy():
            score = board.mark(n)
            if score != -1:
                scores.append(score * n)
                boards.remove(board)
    print(scores[0])
    print(scores[-1])


def read_input(file_name):
    with open(file_name, "r") as f:
        return [x.strip() for x in f.readlines()]


if __name__ == "__main__":
    main()