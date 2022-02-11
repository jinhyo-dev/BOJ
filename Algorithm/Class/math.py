n=int(input())
i=1
open_lockers = []
while (i**2 <=n):
    open_lockers.append(i**2)
    i+=1
print("열린 사물함의 개수는", len(open_lockers))