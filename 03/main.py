# Get our input and format like yesterday
with open("input.txt", 'r') as f:
    contents = repr(f.read())

    # Split and remove starting `'`
    the_map = contents.split("\\n")
    the_map[0] = the_map[0][1:-1]


# Part 1
x = 0
y = 0
trees = 0

while y < len(the_map):
    # If we've gone too far to the right, mod x
    # as the map wraps
    if x >= len(the_map[y]):
        x = x % len(the_map[y])

    if the_map[y][x] == "#":
        trees += 1

    x += 3
    y += 1

print(trees)

#Part 2
x = 0
y = 0
trees = 0
multiple = 1

# Same as above, but chance the increment each time we do the loop
for coord in [[1, 1], [1, 3], [1, 5], [1, 7], [2, 1]]:
    while y < len(the_map):
        if x >= len(the_map[y]):
            x = x % len(the_map[y])

        if the_map[y][x] == "#":
            trees += 1

        x += coord[1]
        y += coord[0]

    multiple *= trees
    trees = 0
    x = 0
    y = 0

print(multiple)