A, B = map(int, input().split())
answer = (str(A//B) + '.')
A = A % B * 10

for _ in range(1000):
  answer += str(A//B)
  A = (A % B)*10

print(answer)