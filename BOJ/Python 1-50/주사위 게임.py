# money = []
# A, B, C = map(int, input().split())
# if A == B == C:
#   money.append(A* 1000 + 10000)
# elif A == B or A == C or B == C:
#   if A == B:
#     money.append(A* 100 + 1000)
#   elif A == C:
#     money.append(A* 100 + 1000)
#   elif B == C:
#     money.append(B* 100 + 1000)
# else:
#   arr = []
#   arr.append(A)
#   arr.append(B)
#   arr.append(C)
#   arr.sort()
#   money.append(arr[-1]*100)
# money.sort()
# print(money[-1])

money = []
for _ in range(int(input())):
    arr = sorted(list(map(int,input().split())))
    if arr[0] == arr[2]:
        money.append(arr[0]*1000+10000)
    elif arr[0] == arr[1] or arr[1] == arr[2]:
        money.append(arr[1]*100+1000)
    else:
        money.append(arr[2]*100)
money.sort()
print(money[-1])