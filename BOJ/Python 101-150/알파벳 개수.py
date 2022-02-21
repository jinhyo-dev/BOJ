alphabet = [0 for _ in range(26)]
word = list(input())
for i in word:
  alphabet[ord(i)-97] += 1
print(*alphabet)