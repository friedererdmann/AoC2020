def get_expenses():
    import os
    curr_dir = os.path.dirname(__file__)
    exp_file_name = "expenses.txt"
    exp_file_path = os.path.join(curr_dir, exp_file_name)

    with open(exp_file_path, "r") as exp_file:
        expenses = [int(line) for line in exp_file.readlines()]

    return expenses

def expenses_part_one():
    expenses = get_expenses()

    for i, x in enumerate(expenses):
        for j, y in enumerate(expenses):
            if i != j and (x + y) == 2020:
                return x * y

print(expenses_part_one())

def expenses_part_two():
    expenses = get_expenses()

    for i, x in enumerate(expenses):
        for j, y in enumerate(expenses):
            for k, z in enumerate(expenses):
                if i != j and i != k and j != k and (x + y + z) == 2020:
                    return x * y * z

print(expenses_part_two())