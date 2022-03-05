def factorial(n):
  if n > 1:
    return n * factorial(n-1)
  else:
    return 1

N = int(input())
tmp = list(str(factorial(N)))
cnt = 0
for i in range(len(tmp)-1, -1, -1):
  if int(tmp[i]) > 0:
    break
  else:
    cnt += 1
print(cnt)