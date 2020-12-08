example = """nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6"""

def get_trees():
    import os
    curr_dir = os.path.dirname(__file__)
    exp_file_name = "instructions.txt"
    exp_file_path = os.path.join(curr_dir, exp_file_name)

    with open(exp_file_path, "r") as exp_file:
        expenses = [line.rstrip() for line in exp_file.readlines()]

    return expenses

code = get_trees()
#code = example.splitlines()

finished = False
for j in range(len(code)):
    lines_visited = []
    acc = 0
    i = 0
    if code[j].startswith("acc"):
        continue
    while True:
        if i >= len(code):
            print(j)
            print("program ran succesfully")
            finished = True
            break
        line = code[i]
        if i == j:
            if line.startswith('nop'):
                line = line.replace('nop', 'jmp')
            if line.startswith('jmp'):
                line = line.replace('jmp', 'nop')
        instruction = line[:3]
        value = int(line[4:])
        if i in lines_visited:
            print("still breaks")
            break
        else:
            lines_visited.append(i)
        if instruction == "nop":
            i += 1
        elif instruction == "acc":
            acc += value
            i += 1
        else:
            i += value
    if finished:
        break

print(acc, i, lines_visited[-2:])