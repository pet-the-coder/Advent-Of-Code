from pprint import pprint


# with open("data/8", 'r') as file:
with open("data/88", 'r') as file:
    adj = [[int(y) for y in x] for x in file.read().split('\n')]

# looking from all directions
heights = [[0 for i in range(len(adj))] for j in range(len(adj[0]))]

w, h = len(heights[0]), len(heights)

for j in range(h):
    # look through that row
    prev = -1
    for i in range(w):
        if prev >= adj[j][i]:
            continue
        prev = adj[j][i]
        heights[j][i] += 1

for j in range(h):
    # look through that row
    prev = -1
    for i in range(w-1, -1, -1):
        if prev >= adj[j][i]:
            continue
        prev = adj[j][i]
        heights[j][i] += 1

# from top
for i in range(w):
    # look through that row
    prev = -1
    for j in range(h):
        if prev >= adj[j][i]:
            continue
        prev = adj[j][i]
        heights[j][i] += 1

# from bottom
for i in range(w):
    # look through that row
    prev = -1
    for j in range(h-1, -1, -1):
        if prev >= adj[j][i]:
            continue
        prev = adj[j][i]
        heights[j][i] += 1


# pprint(heights)
i = 0
for l in heights:
    for n in l:
        if n > 0: i += 1
print(i)


