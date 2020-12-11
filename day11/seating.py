data = """L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL"""

def get_trees():
    import os
    curr_dir = os.path.dirname(__file__)
    exp_file_name = "seats.txt"
    exp_file_path = os.path.join(curr_dir, exp_file_name)

    with open(exp_file_path, "r") as exp_file:
        expenses = [line.rstrip() for line in exp_file.readlines()]
    return expenses

data = data.splitlines()
data = get_trees()
seats = [".{0}.".format(line) for line in data]
h_border = "."*len(seats[0])
seats.append(h_border)
seats.insert(0, h_border)


from itertools import combinations
def get_neighbors(y, x, rows):
    neighbors = []

    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            if i == 0 and j == 0:
                continue
            a = y + i
            b = x + j
            neighbors.append(rows[a][b])

    return neighbors


from itertools import combinations
def get_first_neighbors(y, x, rows):
    neighbors = []

    max_y = len(rows)
    max_x = len(rows[0])
    max_n = max([max_y, max_x])
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            if i == 0 and j == 0:
                continue
            found = False
            for f in range(1, max_n):
                if not found:
                    a = y + (i * f)
                    b = x + (j * f)
                    if 0 < a < max_y and 0 < b < max_x:
                        if rows[a][b] in ["L", "#"]:
                            neighbors.append(rows[a][b])
                            found = True

    return neighbors

def seating_round(rows, max_neighbors, neighbor):
    empty = "L"
    seated = "#"
    floor = "."
    updated_seats = list()
    for y in range(len(rows)):
        row = rows[y]
        updated_row = ""
        for x in range(len(row)):
            c_seat = rows[y][x]
            if c_seat == empty:
                neighbors = neighbor(y, x, rows)
                if not neighbors.count(seated):
                    c_seat = seated
            elif c_seat == seated:
                neighbors = neighbor(y, x, rows)
                if neighbors.count(seated) >= max_neighbors:
                    c_seat = empty
            updated_row += c_seat
        updated_seats.append(updated_row)
    return updated_seats


def part_one(pseats):
    changing = True
    c_result = pseats
    while changing:
        n_result = seating_round(c_result, 4, get_neighbors)
        changing = c_result != n_result
        c_result = n_result

    occupied = 0
    for row in c_result:
        occupied += row.count("#")
    print(occupied)


part_one(seats)

def part_two(pseats):
    changing = True
    c_result = pseats
    while changing:
        '''
        for i, row in enumerate(c_result):
            a = ""
            for n, c in enumerate(row):
                if c == "#":
                    a += str(get_first_neighbors(i, n, c_result).count("#"))
                else:
                    a += c
            print(a)
        '''
        n_result = seating_round(c_result, 5, get_first_neighbors)
        changing = c_result != n_result
        c_result = n_result

    occupied = 0
    for row in c_result:
        occupied += row.count("#")
    print(occupied)

part_two(seats)