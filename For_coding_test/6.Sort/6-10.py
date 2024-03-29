num = int(input())

li = []
for i in range(num):
    li.append(int(input()))

# result = sorted(li, reverse=True)
li.sort(reverse=True)
for i in li:
    print(i, end=' ')