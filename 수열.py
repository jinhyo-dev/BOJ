N, M = map(int, input().split())
arr = list(map(int, input().split()))

sumOfPart = sum(arr[:M])
result = [sumOfPart]

for i in range(0, len(arr)-M):
    sumOfPart = sumOfPart - arr[i] + arr[i+M]
    result.append(sumOfPart)

print(max(result))