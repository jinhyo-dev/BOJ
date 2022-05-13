N, K = map(int, input().split())
string = list(input())
people = 0
for i in range(N):
  if string[i] == 'P':
    for j in range(max(i-K, 0), min(i+K+1, N)):
      if string[j] == 'H':
        string[j] = 'O'
        people += 1
        break
print(people)