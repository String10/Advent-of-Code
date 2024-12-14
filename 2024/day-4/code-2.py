#################### Template ####################
with open("puzzle.txt") as f:
    lines = f.readlines()
#################### Template ####################

data = [line.strip() for line in lines]

n, m = len(data), len(data[0])
to = [[1, 1], [1, -1], [-1, -1], [-1, 1]]
words = ["SSMM", "MSSM", "MMSS", "SMMS"]


def check(x, y):
    if x < 0 or y < 0 or x >= n or y >= m:
        return False
    if data[x][y] != "A":
        return False
    word = ""
    for i in range(4):
        xx = x + to[i][0]
        yy = y + to[i][1]
        if xx < 0 or yy < 0 or xx >= n or yy >= m:
            return False
        word += data[xx][yy]
    return word in words


total = 0
for i in range(n):
    for j in range(m):
        if check(i, j):
            total += 1

print(total)
