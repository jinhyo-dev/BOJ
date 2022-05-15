N, W, H = map(int, input().split())
for _ in range(N):
  num = int(input())
  print('DA' if num ** 2 <= W ** 2 + H ** 2 else 'NE')