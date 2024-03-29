a, b = map(int, input().split())
cnt = 0

while a != 1:
    if a % b == 0:
        a //= b
        cnt += 1
    else:
        a -= 1
        cnt += 1
print(cnt)