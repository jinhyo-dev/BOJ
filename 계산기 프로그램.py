calc = []
total = 0

while True:
  N = input()
  if N == '=':
    break
  calc.append(N)

total += int(calc[0])

for i in range(len(calc)):
  if i % 2:
    if calc[i] == '-':
      total -= int(calc[i+1])
    elif calc[i] == '+':
      total += int(calc[i+1])
    elif calc[i] == '*':
      total *= int(calc[i+1])
    elif calc[i] == '/':
      total //= int(calc[i+1])

print(total)