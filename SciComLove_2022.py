string = ['S', 'c', 'i', 'C', 'o', 'm', 'L', 'o', 'v', 'e']
for _ in range(int(input()) % 10):
  string.append(string[0])
  del string[0]
print(''.join(string))