N = int(input())
arr = list(map(int, input().split()))
sorted_arr = sorted(list(set(arr)))
dic = {sorted_arr[i] : i for i in range(len(sorted_arr))}
for i in arr:
  print(dic[i], end=' ')