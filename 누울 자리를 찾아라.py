import sys
input = sys.stdin.readline

def check_row():
  rtn = 0
  for i in range(N):
    c = 0
    for j in range(N + 1):
      if arr[i][j] == '.':
        c += 1
      else:
        if c >= 2:
          rtn += 1
        c = 0
  return rtn


def check_col():
  rtn = 0
  for j in range(N):
    c = 0
    for i in range(N + 1):
      if arr[i][j] == '.':
        c += 1
      else:
        if c >= 2:
          rtn += 1
        c = 0
  return rtn


N = int(input())
arr = [input() + 'X' for _ in range(N)] + ['X' * (N + 1)]
print(check_row(), check_col())
