def get_trees():
    import os
    curr_dir = os.path.dirname(__file__)
    exp_file_name = "luggage.txt"
    exp_file_path = os.path.join(curr_dir, exp_file_name)

    with open(exp_file_path, "r") as exp_file:
        expenses = [line.rstrip() for line in exp_file.readlines()]

    return expenses


def get_luggage_rules(luggage):
    definition = {}
    for line in luggage:
        color, content = line.split("bags contain ", 2)
        color = color.strip()
        bags = [bag.replace("s,", "").replace(",","").replace("no other","").strip() for bag in content.split("bag")]
        elements = ["s.", ".", ",", ""]
        for el in elements:
            if el in bags:
                bags.remove(el)
        bags_a = [bag[2:] for bag in bags]
        bags_b = list()
        for bag in bags:
            bag_c = bag[2:]
            bag_n = int(bag[0])
            bags_b += [bag_c] * bag_n
        definition[color] = bags_b
    return definition

inputs = '''shiny gold bags contain 2 dark red bags.
dark red bags contain 2 dark orange bags.
dark orange bags contain 2 dark yellow bags.
dark yellow bags contain 2 dark green bags.
dark green bags contain 2 dark blue bags.
dark blue bags contain 2 dark violet bags.
dark violet bags contain no other bags.'''
#definition = get_luggage_rules(inputs.splitlines())
definition = get_luggage_rules(get_trees())

def check_for_content(bag_color):
    list_of_colors = []
    for rule in definition:
        for bag in set(definition[rule]):
            if bag_color in bag:
                list_of_colors.append(rule)
                list_of_colors += check_for_content(rule)
    return list_of_colors

# print(len(set(check_for_content('shiny gold'))))

def find_children(bag_color):
    i = 0
    contents = definition.get(bag_color)
    for each in contents:
        i += 1
        i += find_children(each)
    return i

print(find_children('shiny gold'))
