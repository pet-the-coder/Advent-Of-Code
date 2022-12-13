# following strat plan

WIN = [2, 0, 1]
LOSE = [1, 2, 0]

def outcome(a, b):
    # same
    if b == 1:
        return a + 1 + 3
    # lose
    if b == 0:
        return WIN[a] + 1
    # win
    return LOSE[a] + 6 + 1
    

score = 0
with open("data/2", 'r') as file:
    for line in file.read().split("\n"):
        a, b = line.split()
        # a = rock
        # b = paper
        # c = scissors

        # x = lose
        # y = draw
        # z = win
        # print(a, b)

        # paper > rock > scissors > ...
        a = 0 if a == "A" else 1 if a == "B" else 2
        b = 0 if b == "X" else 1 if b == "Y" else 2
        # print(a, b, outcome(a, b))
        b = outcome(a, b)
        score += b
        # print(a, b, score)
    file.close()
print(score)
