chicken = int(input())
coke, beer = map(int, input().split())
cnt = 0
while chicken > 0:
  if coke >= 2:
    coke -= 2
    chicken -= 1
    cnt += 1
  elif beer >= 1:
    beer -= 1
    chicken -= 1
    cnt += 1
  else:
    break
print(cnt)