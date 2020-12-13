nav = """F10
N3
F7
R90
F11"""
nav = nav.splitlines()

def get_trees():
    import os
    curr_dir = os.path.dirname(__file__)
    exp_file_name = "directions.txt"
    exp_file_path = os.path.join(curr_dir, exp_file_name)

    with open(exp_file_path, "r") as exp_file:
        expenses = [line.rstrip() for line in exp_file.readlines()]
    return expenses

nav = get_trees()

def get_orientation(current, line):
    directions = ["E", "S", "W", "N"]
    letter = line[0]
    amount = int(line[1:])
    if letter not in ["R", "L"]:
        return current
    current = directions.index(current)
    if letter == "R":
        current += int(amount / 90)
    elif letter == "L":
        current -= int(amount / 90)
    current = current % len(directions)
    return directions[current]

def get_movement(orientation, line):
    letter = line[0]
    amount = int(line[1:])
    if letter == "F":
        return orientation, amount
    if letter in ["E", "S", "W", "N"]:
        return letter, amount
    else:
        return orientation, 0

def part_one():
    steps = {"E": 0, "S": 0, "W": 0, "N": 0}
    orientation = "E"
    for row in nav:
        orientation = get_orientation(orientation, row)
        movement, length = get_movement(orientation, row)
        steps[movement] += length
        print(steps)

    manhattan = abs(steps["E"] - steps["W"]) + abs(steps["N"] - steps["S"])
    print(manhattan)

def part_two():
    steps = {"E": 0, "S": 0, "W": 0, "N": 0}
    orientation = "E"

