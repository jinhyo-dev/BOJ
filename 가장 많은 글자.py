import sys
input = sys.stdin.read()
arr = [0] * 26
for i in input:
    if i.islower():
        arr[ord(i)-97] += 1
for j in range(26):
    if arr[j] == max(arr):
        print(chr(97+j), end='')