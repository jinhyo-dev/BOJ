table = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

roman = "MCDXLIV"
number = 0
n = len(roman)
for i in range(n):
    if i < n - 1 and table[roman[i]] < table[roman[i+1]]:
        number -= table[roman[i]]
    else:
        number += table[roman[i]]
print(number)
