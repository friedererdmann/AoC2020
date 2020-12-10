plugs = """28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3"""

def get_trees():
    import os
    curr_dir = os.path.dirname(__file__)
    exp_file_name = "plugs.txt"
    exp_file_path = os.path.join(curr_dir, exp_file_name)

    with open(exp_file_path, "r") as exp_file:
        expenses = [int(line.rstrip()) for line in exp_file.readlines()]
    return expenses

inputs = [int(x) for x in plugs.splitlines()]
#inputs = get_trees()
inputs.sort()
inputs.insert(0,0) # start plug
inputs.insert(len(inputs), max(inputs)+3) # end device
print(inputs)
from collections import Counter
x, y = Counter([inputs[x] - inputs[x-1] for x in range(1,len(inputs))]).values()
print(x*y)

consecutive_lists = []
consecutive_list = []
for i in range(len(inputs)):
    if i+1 < len(inputs):
        if inputs[i+1] - inputs[i] == 1:
            print(inputs[i])
            consecutive_list.append(inputs[i])
        else:
            consecutive_list.append(inputs[i])
            consecutive_lists.append(consecutive_list)
            consecutive_list = []
    else:
        consecutive_list.append(inputs[i])
        consecutive_lists.append(consecutive_list)

print(consecutive_lists)

from itertools import combinations

for llist in consecutive_lists:
    if len(llist) > 2:
        print(llist)
        print(len(llist) // 3)
        print(len(llist) // 4)
