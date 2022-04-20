n = int(input())
gbsw = []
usghs = list(map(int, input().split()))
cnt = 0
for i in range(1, n+1):
  gbsw.append(i)

while gbsw:
  if gbsw[-1] == usghs[0]:
    del gbsw[-1]
    del usghs[0]
  else:
    cnt += 1
    usghs.append(usghs[0])
    del usghs[0]
print(cnt)
