num = int(input())

def sort(ll):
    return ll[1]

li = []
for i in range(num):
    name, score = input().split()
    li.append([name, int(score)])

result = sorted(li, key=sort)

for i in result:
    print(i[0], end=' ')