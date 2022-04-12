for _ in range(int(input())):
  A_Score = 0
  B_Score = 0
  for _ in range(int(input())):
    A, B = input().split()
    if A == B:
      pass
    else:
      if A == 'R' and B == 'P':
        B_Score += 1

      elif A == 'P' and B == 'R':
        A_Score += 1
      
      elif A == 'P' and B == 'S':
        B_Score += 1
      
      elif A == 'S' and B == 'P':
        A_Score += 1
      
      elif A == 'S' and B == 'R':
        B_Score += 1
      
      elif A == 'R' and B == 'S':
        A_Score += 1
      
  if A_Score == B_Score:
    print('TIE')
  
  else:
    print('Player 1' if A_Score > B_Score else 'Player 2')