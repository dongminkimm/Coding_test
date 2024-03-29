row, col = map(int, input().split())
result = 0

for _ in range(row):
    tmp = list(map(int, input().split()))
    min_val = min(tmp)
    result = max(min_val, result)

print(result)