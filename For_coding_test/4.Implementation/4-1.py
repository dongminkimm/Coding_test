num = int(input())

li = input().split()
pos = [1, 1]

for i in li:
    if i == 'R':
        if pos[0] >= num:
            continue
        pos[0] += 1

    elif i == 'L':
        if pos[0] == 1:
            continue
        pos[0] -= 1

    elif i == 'U':
        if pos[1] == 1:
            continue
        pos[1] -= 1

    elif i == 'D':
        if pos[1] >= num:
            continue
        pos[1] += 1
print(pos[1], pos[0])