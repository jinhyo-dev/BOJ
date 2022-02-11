n = int(input())
str = ""
cntDe = 0
cntInde = 0

for i in range(n):
    S = input()
    str += S

table1 = {1: "A", 2: "AN"}
table2 = {3: "THE"}

for ch in str:
    if ch.isalpha():
        upperAlphabet = ch.upper()
        if upperAlphabet in table1:
            cntDe += 1
        elif upperAlphabet in table2:
            cntInde += 1

print(cntDe)
print(cntInde)
