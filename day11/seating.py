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
#data = get_trees()
seats = [".{0}.".format(line) for line in data]
h_border = "."*len(seats[0])
seats.append(h_border)
seats.insert(0, h_border)


from itertools import combinations
def get_neighbors(y, x, rows):
    neighbors = []

    for i, j in combinations([-1, -1, 0, 1, 1], 2):
        a = y + i
        b = x + j
        neighbors.append(rows[a][b])

    return neighbors


def seating_round(rows):
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
                neighbors = get_neighbors(y, x, rows)
                if not neighbors.count(seated):
                    c_seat = seated
            elif c_seat == seated:
                neighbors = get_neighbors(y, x, rows)
                if neighbors.count(seated) >= 4:
                    c_seat = empty
            updated_row += c_seat
        updated_seats.append(updated_row)
    return updated_seats


changing = True
c_result = seats
while changing:
    for i, row in enumerate(c_result):
        output = ""
        for j in range(len(row)):
            c = row[j]
            if c == "#":
                pass
                #c = str(get_neighbors(j, i, c_result).count("#"))
            output += c
        print(output)
    n_result = seating_round(c_result)
    changing = c_result != n_result
    c_result = n_result

occupied = 0
for row in c_result:
    occupied += row.count("#")
print(occupied)