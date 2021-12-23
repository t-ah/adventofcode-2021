import sys


h_index = {"A": 2, "B": 4, "C": 6, "D": 8}
step_cost = {"A": 1, "B": 10, "C": 100, "D": 1000}
cache = {}


def main():
    print("test", step(2, (tuple(11 * [""]), tuple(list("BACDBCDA")))))
    print(step(2, (tuple(11 * [""]), tuple(list("DCBACDAB")))))
    print("test", step(4, (tuple(11 * [""]), tuple(list("BDDACCBDBBACDACA")))))
    print(step(4, (tuple(11 * [""]), tuple(list("DDDCBCBACBADAACB")))))


def step(room_size, state):
    if state in cache:
        return cache[state]
    if state[1] == tuple(room_size * ["A"] + room_size * ["B"] + room_size * ["C"] + room_size * ["D"]):
        return 0
    best_cost = sys.maxsize
    for new_state, step_cost in get_moves(room_size, state):
        best_cost = min(best_cost, step_cost + step(room_size, new_state))
    cache[state] = best_cost
    return best_cost


def get_moves(room_size, state):
    moves = []
    hallway, rooms = state
    for i in range(11):
        if hallway[i] != "":
            occupant = hallway[i]
            h_goal = h_index[occupant]
            if hallway_free(hallway, i, h_goal):
                r_goal = r_index(room_size, occupant)
                for room_offset in reversed(range(room_size)):
                    if rooms[r_goal + room_offset] == "":
                        moves.append((moveH2R(state, i, r_goal + room_offset), path_cost(occupant, abs(h_goal - i) + room_offset + 1)))
                        break
                    elif rooms[r_goal + room_offset] != occupant:
                        break
    for room_entrance_i in range(0, 4 * room_size, room_size):
        for occupant_i in range(room_entrance_i, room_entrance_i + room_size):
            occupant = rooms[occupant_i]
            if occupant == "":
                continue
            if should_leave_room(room_size, rooms, occupant_i):
                entrance = room_to_hallway(room_size, room_entrance_i)
                for hallway_target in [0, 1, 3, 5, 7, 9, 10]:
                    if hallway_free(hallway, entrance, hallway_target):
                        moves.append((moveR2H(state, occupant_i, hallway_target), path_cost(occupant, 1 + (occupant_i % room_size) + abs(entrance - hallway_target))))
            break
    return tuple(moves)


def should_leave_room(room_size, rooms, index):
    occupant = rooms[index]
    depth = index % room_size
    right_room_index = r_index(room_size, occupant)
    if index - depth != right_room_index:
        return True
    for i in range(1, room_size - depth):
        if rooms[index + i] != occupant:
            return True
    return False


def path_cost(who, steps):
    return steps * step_cost[who]


def moveH2R(state, i, j):
    hallway, rooms = list(state[0]), list(state[1])
    rooms[j] = hallway[i]
    hallway[i] = ""
    return (tuple(hallway), tuple(rooms))


def moveR2H(state, i, j):
    hallway, rooms = list(state[0]), list(state[1])
    hallway[j] = rooms[i]
    rooms[i] = ""
    return (tuple(hallway), tuple(rooms))


def hallway_free(hallway, i, goal):
    a, b = (i + 1, goal) if i < goal else (goal, i - 1)
    for j in range(a, b + 1):
        if hallway[j] != "":
            return False
    return True


def r_index(room_size, occupant):
    return (ord(occupant) - 65) * room_size


def room_to_hallway(room_size, room_index):
    return (room_index // room_size) * 2 + 2


if __name__ == "__main__":
    main()