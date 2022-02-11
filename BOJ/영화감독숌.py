arr = []
N = int(input())

for i in range(666, 10000000):
  if '666' in str(i):
    arr.append(i)
print(arr[N-1])