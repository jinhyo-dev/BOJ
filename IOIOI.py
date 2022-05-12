N = int(input())
M = int(input())
string = input()
answer = i = cnt = 0

while i < (M - 1):
  if string[i:i+3] == 'IOI':
    i += 2
    cnt += 1
    if cnt == N:
      answer += 1
      cnt -= 1
  else:
    i += 1
    cnt = 0

print(answer)