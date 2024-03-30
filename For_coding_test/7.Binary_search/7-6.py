# n, m = map(int, input().split())
# li = list(map(int, input().split()))

# li.sort(reverse=True)
# print(li)

# divide = li[0]
# while True:
#     sum = 0
#     for i in li:
#         if i // divide:
#             sum += i % divide
#     if sum < m:
#         divide -= 1
#     elif sum == m:
#         break
# print(divide)

'''
위 방법(내 풀이)로는 실패할 수 있음. 떡의 길이가 10억까지라서 시간 초과 될 가능성 높음
그래서 이진 탐색 알고리즘을 사용해야함.
'''

n, m = map(int, input().split())
array = list(map(int, input().split()))

start = 0
end = max(array)

result = 0
while (start <= end):
    total = 0
    mid = (start + end) // 2
    for x in array:
        if x > mid:
            total += x - mid
    
    if total > m:
        start = mid + 1
    else:
        result = mid
        end = mid - 1
        
print(result)