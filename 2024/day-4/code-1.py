#################### Template ####################
with open("puzzle.txt") as f:
    lines = f.readlines()
#################### Template ####################

data = [line.strip() for line in lines]

n, m = len(data), len(data[0])
to = [[0, 1], [1, 0], [0, -1], [-1, 0], [1, 1], [-1, -1], [1, -1], [-1, 1]]
word = "XMAS"


def check(x, y, t):
    for i in range(4):
        if x < 0 or y < 0 or x >= n or y >= m:
            return False
        if data[x][y] != word[i]:
            return False
        x += to[t][0]
        y += to[t][1]
    return True


total = 0
for i in range(n):
    for j in range(m):
        for k in range(8):
            if check(i, j, k):
                total += 1

print(total)
