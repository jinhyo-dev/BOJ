from collections import deque

N = int(input())
q = deque(i + 1 for i in range(N))
deleted_card = []

while q:
  deleted_card.append(q.popleft())
  if q:
    q.append(q.popleft())

print(*deleted_card)