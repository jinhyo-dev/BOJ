N = int(input())
arr = list(map(int, input().split()))
cnt = 0

def front_swap(array):
  front = 0
  tmp_arr = array
  for i in range(N - 1):
    if tmp_arr[i] % 2 != tmp_arr[i + 1] % 2:
      tmp_arr[i], tmp_arr[i + 1] = tmp_arr[i + 1], tmp_arr[i]
      front += 1
  return front


def back_swap(array):
  back = 0
  tmp_arr = array
  for i in range(N - 1, 0, -1):
    if tmp_arr[i] % 2 != tmp_arr[i - 1] % 2:
      tmp_arr[i - 1], tmp_arr[i] = tmp_arr[i], tmp_arr[i - 1]
      back += 1
  return back


if N == 1:
  print(0)

else:
  print(min(front_swap(arr), back_swap(arr)))
