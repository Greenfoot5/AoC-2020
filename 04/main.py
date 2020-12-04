# Get our input and format like yesterday
with open("input.txt", 'r') as f:
    contents = repr(f.read())

    # Split and remove starting `'`
    contents = contents[1:-1].split("\\n\\n")

valid = 0
valid_passports = []
for item in contents:
    if "byr" in item:
        if "iyr" in item:
            if "eyr" in item:
                if "hgt" in item:
                    if "hcl" in item:
                        if "ecl" in item:
                            if "pid" in item:
                                valid += 1
                                valid_passports.append(item)

print(valid)

# Part 2
passports = []
valid = 0
for passport in valid_passports:
    the_dict = {}
    passport = passport.replace("\\n", " ")
    passport = passport.split(" ")
    for value in passport:
        value = value.split(":")
        the_dict[value[0]] = value[1]
    passports.append(the_dict)

for passport in passports:
    if 1920 <= int(passport['byr']) <= 2002:
        if 2010 <= int(passport['iyr']) <= 2020:
            if 2020 <= int(passport['eyr']) <= 2030:
                if passport['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
                    if len(passport['pid']) == 9:
                        if (150 <= int(passport['hgt'][:-2]) <= 193 and passport['hgt'][-2:] == "cm") or (59 <= int(passport['hgt'][:-2]) <= 76 and passport['hgt'][-2:] == "in"):
                            if passport['hcl'].startswith('#'):
                                print('hcl')
                                hcl_valid = True
                                for char in passport['hcl'][1:]:
                                    if char not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '8', '9', '0', 'a', 'b', 'c', 'd', 'e', 'f']:
                                        hcl_valid = False
                                if hcl_valid:
                                    valid += 1
                                    print(passport)


print(valid)