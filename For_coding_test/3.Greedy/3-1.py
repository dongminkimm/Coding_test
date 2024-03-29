import time

a, b, c = map(int, input().split())
num_list = list(map(int, input().split()))
start_time = time.time()
sum = 0

num_list = sorted(num_list, reverse=True)

while True:
    for i in range(c):
        if b == 0:
            break
        sum += num_list[0]
        b -= 1
    if b == 0:
        break
    sum += num_list[1]
    b -= 1
end_time = time.time()
print(sum)

print(end_time-start_time)