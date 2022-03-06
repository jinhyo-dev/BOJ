problem = []
for _ in range(int(input())):
  title, difficulty = input().split()
  problem.append([difficulty, title])
problem.sort()
print(problem[0][1])