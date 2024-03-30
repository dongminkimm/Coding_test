# 내 풀이
# n = int(input())
# sell = list(map(int, input().split()))

# m = int(input())
# buy = list(map(int, input().split()))

# for item in buy:
#     if item in sell:
#         print("yes", end = ' ')
#     else:
#         print("no", end = ' ')

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
        
        return None
    
n = int(input())
array = list(map(int, input().split()))
array.sort()

m = int(input())
x = list(map(int, input().split()))

for i in x:
    result = binary_search(array, i, 0, n-1)
    if result != None:
        print("yes", end=' ')
    else:
        print('no', end= ' ')