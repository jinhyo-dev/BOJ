import sys
input = sys.stdin.readline

for _ in range(int(input())):
  _ = input()
  note = set(map(int, input().split()))
  _ = input()
  answer = list(map(int, input().split()))
  for i in answer:
    print(1 if i in note else 0)