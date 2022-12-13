with open("data/1", 'r') as file:
    b1, b2, b3 = 0, 0, 0
    add = 0
    for line in file.read().split("\n"):
        if line == "":
            if add < b1:
                if add < b2:
                    b3 = max(add, b3)
                else:
                    b2 = max(add, b2)
            else:
                b1 = max(add, b1)
            add = 0
        else:
            add += int(line)
    print(b1, b2, b3)
    print(sum([b1, b2, b3]))
