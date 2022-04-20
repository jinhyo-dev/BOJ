result = 0
arr = []
for _ in range(4):
    A, B = map(int, input().split())
    result += B - A
    arr.append(result) 
print(max(arr))