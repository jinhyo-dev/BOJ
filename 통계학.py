from collections import Counter 

def is_mode(n):
  cnt = Counter(n).most_common(2)
  if len(n) > 1:
    if cnt[0][1] == cnt[1][1]:
      print(cnt[1][0]) 
    else:
      print(cnt[0][0]) 
  else: print(cnt[0][0])


list = []
n = int(input())
for _ in range(n):
  list.append(int(input()))

list.sort()
print(round(sum(list)/n))
print(list[int(n/2)])
is_mode(list)
print(list[-1] - list[0])