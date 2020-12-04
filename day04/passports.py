import re

class Passport(object):
    def __init__(self, kwargs):
        self.byr = kwargs.get("byr")  # (Birth Year)
        self.iyr = kwargs.get("iyr")  # (Issue Year)
        self.eyr = kwargs.get("eyr")  # (Expiration Year)
        self.hgt = kwargs.get("hgt")  # (Height)
        self.hcl = kwargs.get("hcl")  # (Hair Color)
        self.ecl = kwargs.get("ecl")  # (Eye Color)
        self.pid = kwargs.get("pid")  # (Passport ID)
        self.cid = kwargs.get("cid")  # (Country ID)
        self.valid = False
        self.validate_two()

    def validate(self):
        if self.byr and self.iyr and self.eyr and self.hgt and self.hcl and self.ecl and self.pid:
            self.valid = True

    def validate_two(self):
        if self.byr and self.iyr and self.eyr and self.hgt and self.hcl and self.ecl and self.pid:
            if 1919 < int(self.byr) < 2003:
                if 2009 < int(self.iyr) < 2021:
                    if 2019 < int(self.eyr) < 2031:
                        if (self.hgt.endswith("in") and (58 < int(self.hgt[:-2]) < 77)) or (self.hgt.endswith("cm") and (149 < int(self.hgt[:-2]) < 194)):
                            if self.hcl.startswith("#") and len(self.hcl[1:]) == 6 and re.search("^[0-9a-f]+$", self.hcl[1:]):
                                if self.ecl in ("amb", "blu", "brn", "gry", "grn", "hzl", "oth"):
                                    if len(self.pid) == 9 and self.pid.isdigit():
                                        self.valid = True
                                    else:
                                        print("pid", self.pid)
                                else:
                                    print("ecl", self.ecl)
                            else:
                                print("hcl", self.hcl)
                        else:
                            print("hgt", self.hgt)
                    else:
                        print("eyr", self.eyr)
                else:
                    print("iyr", self.iyr)
            else:
                print("byr", self.byr)


def get_passport_data():
    import os
    curr_dir = os.path.dirname(__file__)
    exp_file_name = "passports.txt"
    exp_file_path = os.path.join(curr_dir, exp_file_name)

    with open(exp_file_path, "r") as exp_file:
        expenses = [line.rstrip() for line in exp_file.readlines()]

    passports = []
    passport_data = ""
    for line in expenses:
        if line:
            passport_data += " " + line
        if not line:
            passport_dict = {}
            passport_entries = passport_data.lstrip().split(" ")
            for entry in passport_entries:
                key, value = entry.split(":")
                passport_dict[key] = value
            passports.append(Passport(passport_dict))
            passport_data = ""
    return passports

passports = get_passport_data()
print(len(passports))
i = 0
for passport in passports:
    if passport.valid:
        i += 1
print(i)