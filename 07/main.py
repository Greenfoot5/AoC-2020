# Get our input and format like yesterday
with open("input.txt", 'r') as f:
    contents = repr(f.read())

    # Split and remove starting `'`
    contents = contents[1:-1].split("\\n")

# Part 1

bags = {}
for item in contents:
    items = item.split(" contain ")
    bag_types = items[1][:-1].split(", ")
    items[0] = items[0].replace(' bags', "")
    items[0] = items[0].replace(' bag', "")
    for bag in bag_types:
        bag = bag.replace(" bags", "")
        bag = bag.replace(" bag", "")
        try:
            bags[bag[2:]].append(items[0])
        except KeyError:
            bags[bag[2:]] = [items[0]]

bag_count = 0
bag_types = ["shiny gold"]
index = 0
while index < len(bag_types):
    try:
        for bag in bags[bag_types[index]]:
            if bag != "no other" and bag not in bag_types:
                bag_count += 1
                bag_types.append(bag)
    except KeyError:
        pass
    index += 1

print(bag_count)

# Part 2

bags = {}
for item in contents:
    items = item.split(" contain ")
    items[0] = items[0].replace(' bags', "")
    items[0] = items[0].replace(' bag', "")
    bags[items[0]] = []
    items[1] = items[1][:-1].split(", ")
    for bag in items[1]:
        try:
            for i in range(int(bag[0])):
                bag = bag.replace(" bags", "")
                bag = bag.replace(" bag", "")
                bags[items[0]].append(bag[2:])
        except ValueError:
            pass

bag_count = 0
bag_types = ["shiny gold"]
index = 0
while index < len(bag_types):
    try:
        for bag in bags[bag_types[index]]:
            if bag != "no other":
                bag_count += 1
                bag_types.append(bag)
    except KeyError:
        pass
    index += 1

print(bag_count)
