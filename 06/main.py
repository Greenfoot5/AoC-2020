# Get our input and format like yesterday
with open("input.txt", 'r') as f:
    contents = repr(f.read())

    # Split and remove starting `'`
    contents = contents[1:-1].split("\\n\\n")

character_count = 0
for item in contents:
    one_string = item.replace("\\n", "")
    character_count += len("".join(set(one_string)))

print(character_count)

duplicate_count = 0
for item in contents:
    one_string = item.split("\\n")
    for char in one_string[0]:
        count = 0
        for part in one_string:
            if char in part:
                count += 1
        if count >= len(one_string):
            duplicate_count += 1

print(duplicate_count)
