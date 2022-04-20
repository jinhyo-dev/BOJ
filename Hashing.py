N = int(input())
str = input()
answer = 0
for i in range(N):
  answer += (ord(str[i] )-96) * (31 ** i)
print(answer % 1234567891)