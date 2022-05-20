from sys import stdin
input = stdin.readline
colorPaper = [list(map(int, input().split())) for _ in range(int(input()))]

white = blue = 0

def count_of_paper(x, y, n):
  global white, blue
  piece_of_paper = colorPaper[x][y]
  for i in range(x, x+n):
    for j in range(y, y+n):
      if colorPaper[i][j] != piece_of_paper:
        count_of_paper(x, y, n//2)
        count_of_paper(x, y + n//2, n//2)
        count_of_paper(x + n//2, y, n//2)
        count_of_paper(x + n//2, y + n//2, n//2)
        return
  if piece_of_paper == 1:
    blue += 1
    return
  else:
    white += 1
    return

count_of_paper(0, 0, len(colorPaper))
print(white, blue, sep='\n')