x = int(input())
array = list(map(int, input().split()))

d = [0] * 101

d[0] = array[0]
d[1] = max(array[0], array[1])

for i in range(2, x):
    d[i] = max(d[i-1], d[i-2]+array[i])

print(d[x-1])
