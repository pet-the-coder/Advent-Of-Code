from pprint import pprint

def compile_position(x, y):
    return x * 100000 + y

def decompile_position(num):
    return (num // 100000, num % 100000)

def to_far(p1, p2):
    return abs(p1[0] - p2[0]) > 1 or abs(p1[1] - p2[1]) > 1

def handle_move(target, init) -> list:
    # manipulate data in "init"
    dx = target[0] - init[0]
    dy = target[1] - init[1]
    # print("dxy: ", dx, dy)
    # diagonal cases first
    # topright
    if (dx > 0 and dy > 1) or (dx > 1 and dy > 0):
        init[1] += 1
        init[0] += 1
        # print('topright')
    # topleft
    elif (dx < 0 and dy > 1) or (dx < -1 and dy > 0):
        init[1] += 1
        init[0] -= 1
        # print('topleft')
    # bottom right
    elif (dx > 0 and dy < -1) or (dx > 1 and dy < 0):
        init[0] += 1
        init[1] -= 1
        # print('botright')
    elif (dx < 0 and dy < -1) or (dx < -1 and dy < 0):
        init[0] -= 1
        init[1] -= 1
        # print('botleft')
    # unidirectional cases next
    elif dx == 2:
        init[0] += 1
    elif dx == -2:
        init[0] -= 1
    elif dy == 2:
        init[1] += 1
    elif dy == -2:
        init[1] -= 1

d4 = {"R": (1, 0), "U": (0, 1), "L": (-1, 0), "D": (0, -1)}
p4 = set()

POINTS = [[1000, 1000] for i in range(10)]
HEAD_POS = [1000, 1000]
TAIL_POS = [1000, 1000]
TRAVEL = 0


# with open("test", 'r') as file:
with open("9", 'r') as file:
    steps = file.read().split("\n")

for step in steps:
    dn, ds = step.split()
    for i in range(int(ds)):
        # move the head
        POINTS[0][0] += d4[dn][0]
        POINTS[0][1] += d4[dn][1]
        for i in range(len(POINTS)-1):
            # move tail position
            if to_far(POINTS[0], POINTS[i+1]):
                # do something to reduce distance
                handle_move(POINTS[i], POINTS[i+1])
            # print(HEAD_POS[0] - 1000, HEAD_POS[1] - 1000, "|", TAIL_POS[0]-1000, TAIL_POS[1]-1000)
            # print(i+1, ": ", POINTS[0][0] - 1000, POINTS[0][1] - 1000, "|", POINTS[i+1][0]-1000, POINTS[i+1][1]-1000)
            # add tail visited position
            if i == 8:
                p4.add(compile_position(POINTS[9][0], POINTS[9][1]))
        # print('-'*20)


# pprint(p4)
pprint(len(p4))


