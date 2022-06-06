def collatz_A(number):
  if number == 1:
    return 0
  elif number % 2 == 0:
    arr_A.append(number // 2)
    return collatz_A(number // 2)
  else:
    arr_A.append(3 * number + 1)
    return collatz_A(3 * number + 1)

def collatz_B(number):
  if number == 1:
    return 0
  elif number % 2 == 0:
    arr_B.append(number // 2)
    return collatz_B(number // 2)
  else:
    arr_B.append(3 * number + 1)
    return collatz_B(3 * number + 1)

while True:
  A, B = map(int, input().split())
  arr_A = [A]
  arr_B = [B]
  if A == 0 and B == 0:
    break
  isPrint = False
  collatz_A(A)
  collatz_B(B)
  for i in range(len(arr_A)):
    for j in range(len(arr_B)):
      if arr_A[i] == arr_B[j]:
        print(f'{A} needs {i} steps, {B} needs {j} steps, they meet at {arr_A[i]}')
        isPrint = True
        break
    if isPrint:
      break