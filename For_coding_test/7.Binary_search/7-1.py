def sequential_search(n, target, array):
    for i in range(n):
        if array[i] == target:
            return i+1
        
print("생성할 원소 개수와 찾을 문자열 입력")
n, target = input().split()
n = int(n)

print("앞서 작성한 개수만큼 문자열 입력")
array = input().split()

print(sequential_search(n, target, array))