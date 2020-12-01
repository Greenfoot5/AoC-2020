with open("input.txt", 'r') as f:
    contents = repr(f.read())

    numbers = contents[1:-1].split("\\n")
    print(numbers)
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
