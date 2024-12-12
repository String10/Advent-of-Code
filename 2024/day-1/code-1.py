with open("puzzle.txt") as f:
    data = f.read().splitlines()

data = [x.split(" ")[::3] for x in data]

col_0 = [x[0] for x in data]
col_1 = [x[1] for x in data]

new_data = list(zip(sorted(col_0), sorted(col_1)))

total = 0
for i in range(len(new_data)):
    total += abs(int(new_data[i][0]) - int(new_data[i][1]))

print(total)
