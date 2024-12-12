# copied from p1

with open("puzzle.txt") as f:
    data = f.read().splitlines()

data = [x.split(" ")[::3] for x in data]

col_0 = [x[0] for x in data]
col_1 = [x[1] for x in data]

new_data = list(zip(sorted(col_0), sorted(col_1)))

# end

num = len(data)

total, l_pos, r_pos = 0, 0, 0

while l_pos < num and r_pos < num and new_data[l_pos][0] < new_data[r_pos][1]:
    l_pos += 1

while l_pos < num and r_pos < num:
    while r_pos < num and new_data[l_pos][0] > new_data[r_pos][1]:
        r_pos += 1
    while r_pos < num and new_data[l_pos][0] == new_data[r_pos][1]:
        total += int(new_data[l_pos][0])
        r_pos += 1
    l_pos += 1

print(total)
