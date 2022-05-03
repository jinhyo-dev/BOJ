A, B = map(int, input().split())
price = int(input())
if A + B >= price * 2:
    print(A + B - (price * 2))
else:
    print(A+B)