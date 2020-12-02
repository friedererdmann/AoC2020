class Password(object):
    def __init__(self, **kwargs):
        self.min = 0
        self.max = 1
        self.letter = "a"
        self.password = "abc"
        self.valid = False
        if kwargs.get('line'):
            self.from_line(kwargs['line'])
        # self.validate()
        self.validate_new()

    def from_line(self, line):
        inputs = line.split(" ")
        self.min, self.max = [int(i) for i in inputs[0].split("-")]
        self.letter = inputs[1][0].lower()
        self.password = inputs[2]

    def validate(self):
        if self.min <= self.password.count(self.letter) <= self.max:
            self.valid = True

    def validate_new(self):
        if (self.password[self.min-1] == self.letter) != (self.password[self.max-1] == self.letter):
            self.valid = True


def get_file_data():
    import os
    curr_dir = os.path.dirname(__file__)
    exp_file_name = "inputs.txt"
    exp_file_path = os.path.join(curr_dir, exp_file_name)

    with open(exp_file_path, "r") as exp_file:
        expenses = [Password(line=line) for line in exp_file.readlines()]

    return expenses


i = 0
for password in get_file_data():
    if password.valid:
        i += 1
print(i)