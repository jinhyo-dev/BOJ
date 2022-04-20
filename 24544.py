N = int(input())
sumOfNotInMyView = 0
contents = list(map(int, input().split()))
MyView = list(map(int, input().split()))

for i in range(N):
  if MyView[i] == 0:
    sumOfNotInMyView += contents[i]

print(sum(contents), sumOfNotInMyView, sep='\n')