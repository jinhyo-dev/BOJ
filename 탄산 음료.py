e, f, c = map(int, input().split())
bottles = e + f
newBottles = 0
while bottles >= c:
  newBottles += bottles // c
  bottles = bottles // c + bottles % c
print(newBottles)