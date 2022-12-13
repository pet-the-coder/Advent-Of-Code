from sys import stdin

with open("10", 'r') as file:
# with open("t", 'r') as file:
    data = file.read().split('\n')

WIDTH = 40
HEIGHT = 6
SCREEN = ""

SIGNALS = []
def update_screen(c, x):
    global SCREEN
    cc = c%40
    val = cc-1 <= x <= cc + 1
    print(f"CYCLE: {c} | REGISTER: {x} | DRAW: {'      ' if val else '+=++++'}")
    if val:
        SCREEN += '#'
    else:
        SCREEN += '.'

def check_important(c, x):
    # do some checks :)
    if (c-20)%40 == 0:
        SIGNALS.append(c * x)
        # print("Signal:", c * x)

cycle = 0
X = 1
for operation in data:
    c = operation.split()
    if len(c) > 1:
        a, b = c[0], c[1]
        b = int(b)
    else:
        a = c[0]
    # perform cycle operations
    if a == "addx":
        for i in range(2):
            update_screen(cycle, X)
            cycle += 1
            check_important(cycle, X)
        X += b
    else:
        update_screen(cycle, X)
        cycle += 1
        check_important(cycle, X)

print("TOTAL:", sum(SIGNALS))
for i in range(0, WIDTH*HEIGHT, WIDTH):
    print(SCREEN[i:i+40])
