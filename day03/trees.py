def get_trees():
    import os
    curr_dir = os.path.dirname(__file__)
    exp_file_name = "trees.txt"
    exp_file_path = os.path.join(curr_dir, exp_file_name)

    with open(exp_file_path, "r") as exp_file:
        expenses = [line.rstrip() for line in exp_file.readlines()]

    return expenses

def traverse_trees(right=3, down=1):
    tree_map = get_trees()
    length = len(tree_map[0])
    depth = len(tree_map)
    x = 0
    y = 0
    trees = 0
    while y < depth:
        if x > length - 1:
            x = x % (length)
        character = "O"
        if tree_map[y][x] == "#":
            trees += 1
            character = "X"
        # print(tree_map[y][:x-1]+character+tree_map[y][x:])
        y += down
        x += right
    return trees

a = map(lambda args: traverse_trees(*args), [(1,1), (3,1), (5,1), (7,1), (1,2)])

print(traverse_trees())
from functools import reduce
print(reduce((lambda x, y: x * y), a))

