words = [input() for _ in range(int(input()))]
dict = {}

for word in words:
  sqrt = len(word) - 1
  for i in word:
    if i in dict:
      dict[i] += pow(10, sqrt)
    else:
      dict[i] = pow(10, sqrt)
    sqrt -= 1

dict = sorted(dict.values(), reverse=True)
result, n = 0, 9

for i in dict:
  result += i * n
  n -= 1

print(result)