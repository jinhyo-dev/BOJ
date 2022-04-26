for _ in range(int(input())):
  A, B = input().split()
  A_arr = list(A)
  B_arr = list(B)
  A_arr.sort()
  B_arr.sort()
  if ''.join(A_arr) == ''.join(B_arr):
    print(f'{A} & {B} are anagrams.')
  else:
    print(f'{A} & {B} are NOT anagrams.')