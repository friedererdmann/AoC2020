def get_customs():
    import os
    curr_dir = os.path.dirname(__file__)
    exp_file_name = "customs.txt"
    exp_file_path = os.path.join(curr_dir, exp_file_name)

    with open(exp_file_path, "r") as exp_file:
        #expenses = [line.rstrip() for line in exp_file.readlines()]
        expenses = exp_file.read()

    return expenses

answers = """abc

a
b
c

ab
ac

a
a
a
a

b
"""

answers = get_customs()
import collections
yes = 0
for answer in answers.split("\n\n"):
    participants = len(answer.splitlines())
    answer_list = list(answer.replace("\n", ""))
    print(participants, answer_list)
    counted_list = collections.Counter(answer_list)
    for element in counted_list:
        if counted_list[element] == participants:
            yes += 1
    # yes += len(set(answer.replace("\n", "")))

print(yes)