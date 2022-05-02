for _ in range(int(input())):
  N = int(input())
  answer = 0
  for i in range(1, N):
    if i ** 2 <= N:
      answer += 1
    if i ** 2 > N:
      break
  print(answer)