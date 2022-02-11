from fractions import Fraction
N = int(input())
arr = list(map(int, input().split()))
for i in range(1, N):
  f = arr[0] / arr[i]
  fraction = str(Fraction(f).limit_denominator())
  try:
    if int(fraction) % 1 == 0:
      pass 
    print(f'{fraction}/1')
  except:
    print(fraction)
  
# from math import gcd
# N = int(input())
# arr = list(map(int, input().split()))
# for i in range(1, N):
#   G = gcd(arr[0], arr[i])
#   print('{0}/{1}'.format(arr[0] // G, arr[i] // G))