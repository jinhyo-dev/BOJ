n = int(input())
str = ""

for i in range(n):
    S = input()
    str += S

table = {}

for a in str:
    if a.isalpha():
        upperAlphabet = a.upper()
        if upperAlphabet not in table:
            table[upperAlphabet] = 1
        else:
            table[upperAlphabet] += 1

max = 0

for total in table:
    if max < table[total]:
        max = table[total]

print(max)
