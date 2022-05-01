tiles = [0, 1, 2]
for i in range(3, 1001):
  tiles.append(tiles[i-2] + tiles[i-1])
N = int(input())
print(tiles[N] % 10007)
