arr = list(map(int, input().split()))
Vnum = 0
for i in arr:
  Vnum += i**2 
print(Vnum %  10)