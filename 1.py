def solution(n):
    if n == 1:
        return 1
    num = cnt = 1
    while True:
      num = num * 10 + 1
      cnt += 1
      if num % n == 0:
        return cnt

while True:
  try:
    N = int(input())
  except EOFError:
    break
  print(solution(N))
