n, m = map(int, input().split())

result = 0
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b, cost = map(int, input().split())
    graph[a].append((cost, b))

for i in graph:
    i.sort()

print(graph)