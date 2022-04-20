import sys
N = sys.stdin.readline()
find_arr = set(sys.stdin.readline().split())
M = sys.stdin.readline()
arr = sys.stdin.readline().split()

for i in arr:
  sys.stdout.write('1\n') if i in find_arr else sys.stdout.write('0\n')
