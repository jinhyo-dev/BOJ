h1, m1, s1 = map(int, input().split(':'))
h2, m2, s2 = map(int, input().split(':'))
now = h1 * 3600 + m1 * 60 + s1
start = h2 * 3600 + m2 * 60 + s2
result = 0

if now > start:
  result = 24 * 3600 - (now - start)
else:
  result = start - now

h = result // 3600
m = result // 60 % 60
s = result % 60
print(f'{h:02d}:{m:02d}:{s:02d}')
