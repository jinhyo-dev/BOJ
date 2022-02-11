arr = list(map(int, input().split()))
sorted_arr = sorted(arr)
re_sorted_arr = sorted(arr, reverse=True)
if arr == sorted_arr:
  print('ascending')
elif arr == re_sorted_arr:
  print('descending')
else:
  print('mixed')