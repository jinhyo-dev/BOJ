N = int(input())
cnt = 0
i =0
while True:
  i += 1
  cnt += i  
  if cnt > N:
    print(i-1)
    break