import sys
input = sys.stdin.readline
N = int(input())
stack = []
arr = []
k = 1
boolean = True

for i in range(N):
    num = int(input())
    while k <= num:
        stack.append(k)
        arr.append('+')
        k += 1
    
    if stack[-1] == num:
        stack.pop()
        arr.append('-')
    else:
        print('NO')
        boolean = False
        break

if boolean == True:
    for i in arr:
        print(i)
