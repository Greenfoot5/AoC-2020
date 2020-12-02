# Load the input from file
with open("input.txt", 'r') as f:
    # Break up the fine
    contents = repr(f.read())
    # Random `'` at the start and end
    numbers = contents[1:-1].split("\\n")

    # Turn into ints
    for i in range(len(numbers)):
        numbers[i] = int(numbers[i])

# Part 1
for num_a in numbers:
    for num_b in numbers:
        if num_a + num_b == 2020:
            print(num_a * num_b)

# Part 2
for num_a in numbers:
    for num_b in numbers:
        for num_c in numbers:
            if num_a + num_b + num_c == 2020:
                print(num_a * num_b * num_c)
