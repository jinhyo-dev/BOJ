for _ in range(int(input())):
  candidate = [int(input()) for _ in range(int(input()))]
  sortedCandidate = sorted(candidate, reverse=True)
  if sortedCandidate[0] == sortedCandidate[1]:
    print('no winner')
  elif sum(candidate) // 2 >= sortedCandidate[0]:
    print(f'minority winner {candidate.index(sortedCandidate[0]) + 1}')
  else:
    print(f'majority winner {candidate.index(sortedCandidate[0]) + 1}')