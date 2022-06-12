N = input()
lenOfN = len(N) - 1
answer = 0

for i in range(lenOfN):
  answer += 9 * (10 ** i) * (i + 1)
  i += 1
answer += (int(N) - (10 ** lenOfN) + 1) * (lenOfN + 1)
print(answer)