price = []

def solution(arr):
  if len(set(arr)) == 1:
    return 50000 + (arr[0] * 5000)
  if len(set(arr)) == 2:
    if arr[1] == arr[2]:
      return 10000 + arr[1] * 1000
    else:
      return 2000 + (arr[0] * 500) + (arr[2] * 500)

  for i in range(3):
    if arr[i] == arr[i+1]:
      return 1000 + arr[i] * 100
  return arr[3] * 100

for _ in range(int(input())):
  dice = sorted(list(map(int, input().split())))
  price.append(solution(dice))

print(max(price))