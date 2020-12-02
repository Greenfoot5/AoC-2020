import operator

# Get our input and format like yesterday
with open("input.txt", 'r') as f:
    contents = repr(f.read())

    # Split and remove starting `'`
    passwords = contents.split("\\n")
    passwords[0] = passwords[0][1:]

# Part 1
valid_passwords = 0
# Go through each of the passwords
for password in passwords:
    password = password.split(" ")
    password[0] = password[0].split("-")

    # Get the char count of specified char
    count = 0
    for char in password[2]:
        if char == password[1][0]:
            count += 1

    # If char count if valid, the password is
    if int(password[0][1]) >= count >= int(password[0][0]):
        valid_passwords += 1

print(valid_passwords)

# Part 2
valid_passwords = 0
for password in passwords:
    # Password formatting
    password = password.split(" ")
    password[0] = password[0].split("-")

    # Get the selected char
    char = password[1][0]

    # Check the chars at each position is valid
    index_a = password[2][int(password[0][0]) - 1] == char
    index_b = password[2][int(password[0][1]) - 1] == char

    # Check only one is true
    if operator.xor(index_a, index_b):
        valid_passwords += 1

print(valid_passwords)