import operator

passwords = []
with open("input.txt", 'r') as f:
    contents = repr(f.read())

    passwords = contents.split("\\n")
    passwords[0] = passwords[0][1:]

# Part 1
valid_passwords = 0
for password in passwords:
    password = password.split(" ")
    password[0] = password[0].split("-")

    count = 0
    for char in password[2]:
        if char == password[1][0]:
            count += 1

    if int(password[0][1]) >= count >= int(password[0][0]):
        valid_passwords += 1

print(valid_passwords)

# Part 2
valid_passwords = 0
for password in passwords:
    password = password.split(" ")
    password[0] = password[0].split("-")
    char = password[1][0]

    index_a = password[2][int(password[0][0]) - 1] == char
    index_b = password[2][int(password[0][1]) - 1] == char

    if operator.xor(index_a, index_b):
        valid_passwords += 1

print(valid_passwords)