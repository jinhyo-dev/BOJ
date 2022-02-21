vowels = ['a', 'e', 'i', 'o', 'u']
words = list(input())
cnt = 0
for word in words:
  if word in vowels:
    cnt += 1
print(cnt)