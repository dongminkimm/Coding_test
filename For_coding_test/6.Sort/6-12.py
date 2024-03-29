'''
내 풀이

n, k = map(int, input().split())

array = []
for i in range(2):
    array.append(list(map(int, input().split())))

for i in range(k):
    min_idx = array[0].index(min(array[0]))
    max_idx = array[1].index(max(array[1]))

    if array[0][min_idx] <= array[1][max_idx]:
        array[0][min_idx], array[1][max_idx] = array[1][max_idx], array[0][min_idx]

print(sum(array[0]))
'''

n, k = map(int, input().split())
ar1 = list(map(int, input().split()))
ar2 = list(map(int, input().split()))

ar1.sort()
ar2.sort(reverse=True)

for i in range(k):
    if ar1[i] < ar2[i]:
        ar1[i], ar2[i] = ar2[i], ar1[i]
    else:
        break
print(sum(ar1))