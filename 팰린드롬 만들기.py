palindrome = []
string = list(input())
for _ in range(len(string)):
  string.append(string[0])
  del string[0]
  if string == string[::-1]:
    palindrome.append(''.join(string))
print(min(palindrome))