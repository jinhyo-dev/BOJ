N = int(input())
arr = list(map(int, input().split()))
answer = [arr[0]]
for i in range(1, N):
  answer.append((arr[i] * (i + 1)) - sum(answer))
print(*answer)