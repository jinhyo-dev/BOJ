from sys import stdin
input = stdin.readline
N = int(input())
students = []

for _ in range(N):
  S = list(input().split())
  students.append([S[0], int(S[1]), int(S[2]), int(S[3])])

students.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))

for s in students:
  print(s[0])