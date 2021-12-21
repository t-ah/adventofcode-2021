from functools import cache


def main():
    positions = [1, 3]

    players = [Player(p) for p in positions]
    final_die = playTo1000(players)
    scores = [p.score for p in players]
    print(min(scores) * final_die)

    print(max(count_universes(positions[0] - 1, 0, positions[1] - 1, 0, 0)))


@cache
def count_universes(p1_pos, p1_score, p2_pos, p2_score, player_index):
    if p1_score >= 21:
        return (1, 0)
    if p2_score >= 21:
        return (0, 1)
    result = [0, 0]
    for d1 in range(1, 4):
        for d2 in range(1, 4):
            for d3 in range(1, 4):
                d = d1 + d2 + d3
                np1_pos, np1_score, np2_pos, np2_score = p1_pos, p1_score, p2_pos, p2_score
                if player_index == 0:
                    np1_pos = (np1_pos + d) % 10
                    np1_score += np1_pos + 1
                else:
                    np2_pos = (np2_pos + d) % 10
                    np2_score += np2_pos + 1
                r = count_universes(np1_pos, np1_score, np2_pos, np2_score, (player_index + 1) % 2)
                for i in range(2):
                    result[i] += r[i]
    return tuple(result)


def playTo1000(players):
    die = 1
    while True:
        for p in players:
            p.advance(3 * die + 3)
            die += 3
            if p.score >= 1000:
                return die - 1


class Player:
    def __init__(self, pos):
        self.pos = pos - 1
        self.score = 0

    def advance(self, n):
        self.pos = (self.pos + n) % 10
        self.score += self.pos + 1


if __name__ == "__main__":
    main()