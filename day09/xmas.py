test_data="""35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576"""

def get_trees():
    import os
    curr_dir = os.path.dirname(__file__)
    exp_file_name = "xmas.txt"
    exp_file_path = os.path.join(curr_dir, exp_file_name)

    with open(exp_file_path, "r") as exp_file:
        expenses = [int(line.rstrip()) for line in exp_file.readlines()]

    return expenses

from itertools import combinations

def get_invalid_number(test_lines, test_length):
    

    for i in range(test_length,len(test_lines)):
        #print(test_lines[i], test_lines[i-test_length:i])
        valid = [x for x in combinations(test_lines[i-test_length:i], 2) if sum(x) == test_lines[i]]
        # peanuts, walnuts, hazelnuts, coconuts - it's a sound idea ;)
        #print(valid)
        if not valid:
            return(test_lines[i])
            break


ex_lines = [int(x) for x in test_data.splitlines()]
real_lines = get_trees()
# print(get_invalid_number(ex_lines, 5))
invalid_number = (get_invalid_number(real_lines, 25))

def get_weakness(test_elements):
    for i in range(len(test_elements)):
        for j in range(len(test_elements)):
            if i == j:
                continue
            line = test_elements[i:j]
            if sum(line) == invalid_number:
                print("Consecutive Numbers", line)
                print("Max", max(line))
                print("Min", min(line))
                print("Sum", sum([max(line), min(line)]))
                break


get_weakness(real_lines)