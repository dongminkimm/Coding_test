n, m = map(int, input().split())

result = []
parent = [0] * (n+1)

for i in range(1, n+1):
    parent[i] = i

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


for _ in range(m):
    fn, a, b = map(int, input().split())
    if fn == 0:
        union_parent(parent, a, b)
    elif fn == 1:
        check_a = find_parent(parent, a)
        check_b = find_parent(parent, b)
        if check_a == check_b:
            result.append("YES")
        else:
            result.append("NO")
            

for i in result:
    print(i)