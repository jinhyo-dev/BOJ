N = int(input())
tower = list(map(int, input().split()))
answer = 0

for i in range(1, N-1):
  tmp = tower[i] + min(tower[i-1], tower[i+1])
  answer = max(answer, tmp)

answer = max(answer, tower[0])
answer = max(answer, tower[-1])
print(answer)