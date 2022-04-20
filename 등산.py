N = int(input())
height = list(map(int, input().split()))
for i in range(N):
  if height[i] >= height[i+1]:
    print(height[i])
    break