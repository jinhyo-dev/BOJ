from ast import Lambda


L, R, A = map(int, input().split())

while A:
  if L < R:
    L += 1
  else:
    R += 1
  A -= 1

print(L + R - abs(L - R))