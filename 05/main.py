# Get our input and format like yesterday
with open("input.txt", 'r') as f:
    contents = repr(f.read())

    # Split and remove starting `'`
    contents = contents[1:-1].split("\\n")

for i in range(len(contents)):
    binary_num = ""
    for j in range(len(contents[i])):
        if contents[i][j] == "F":
            binary_num += "0"
        elif contents[i][j] == "B":
            binary_num += "1"
        elif contents[i][j] == "L":
            binary_num += "0"
        elif contents[i][j] == "R":
            binary_num += "1"
    contents[i] = binary_num

pass_codes = []
highest = 0
for item in contents:
    result = 0
    result += int(item[:-3], 2) * 8
    result += int(item[-3:], 2)
    pass_codes.append(result)
    if result > highest:
        highest = result

full_plane = []
for i in range(839):
    full_plane.append(i)

for i in range(len(pass_codes)):
    full_plane[pass_codes[i]] = 0

for code in full_plane:
    if code != 0:
        print(code)

print(pass_codes)
print(highest)