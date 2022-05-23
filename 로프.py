ropes = []
for _ in range(int(input())):
  ropes.append(int(input()))
ropes.sort(reverse=True)

for i in range(len(ropes)):
  ropes[i] *= (i + 1)

print(max(ropes))