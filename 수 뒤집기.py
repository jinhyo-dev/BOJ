for _ in range(int(input())):
  N = input()
  S = int(N) + int(N[::-1])
  print('YES' if str(S) == str(S)[::-1] else 'NO')