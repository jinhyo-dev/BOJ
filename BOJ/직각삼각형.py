longest = 0
shortSide = 0
while True:
  A, B, C = map(int, input().split())
  if A == B == C == 0:
    break
  if A > B and A > C:
    longest = A**2
    shortSide = (B**2 + C**2)
  elif B > C and B > A:
    longest = B**2
    shortSide = (A**2 + C**2)
  elif C > A and C > B:
    longest = C**2
    shortSide = (B**2 + A**2)
  
  if longest == shortSide:
    print("right")
  else:
    print('wrong')
  