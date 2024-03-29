n, m = map(int, input().split())
x, y, look = map(int, input().split())

d = [[0]*m for _ in range(n)]

# create map
array = []
for _ in range(n):
    array.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def turn_left():
    global look
    look -= 1
    if look == -1:
        look = 3

cnt = 1
turn_time = 0
while True:
    turn_left()
    nx = x + dx[look]
    ny = y + dy[look]

    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        cnt += 1
        turn_time = 0
        continue
    else:
        turn_time += 1

    if turn_time == 4:
        nx = x - dx[look]
        ny = y - dy[look]

        if array[nx][ny] == 0:
            x = nx
            y = ny
        else:
            break
        turn_time = 0
print(cnt)