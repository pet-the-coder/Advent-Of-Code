
initial = [
    list([x for x in "GFVHPS"]),
    list([x for x in "GJFBVDZM"]),
    list([x for x in "GMLJN"]),
    list([x for x in "NGZVDWP"]),
    list([x for x in "VRCB"]),
    list([x for x in "VRSMPWLZ"]),
    list([x for x in "THP"]),
    list([x for x in "QRSNCHZV"]),
    list([x for x in "FLGPVQJ"])
]

# initial = [
#     list([x for x in "ZN"]),
#     list([x for x in "MCD"]),
#     list([x for x in "P"])
# ]

# figure out how to parse
input_ = """
    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 """


def move(count, f, t):
    global initial
    buffer = []
    for i in range(count):
        buffer.append(initial[f].pop())
    # add to new
    initial[t] += reversed(buffer)

with open("data/5", 'r') as file:
# with open("data/t", 'r') as file:
    for line in file.read().split('\n'):
        action, count, _, f, _, t = line.split()
        count = int(count)
        f = int(f)-1
        t = int(t)-1
        # move
        move(count, f, t)

[print(x[-1], end="") for x in initial] 
print()


