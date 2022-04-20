def get_stars(n):
  list = []
  for i in range(3 * len(n)):
    if i // len(n) ==  1:
      list.append(n[i % len(n)] + " " * len(n) + n[i % len(n)])
    else:
      list.append(n[i % len(n)] * 3)
  return list



stars = ["***", "* *", "***"]
n = int(input())
k = 0

while n != 3:
  n = int(n / 3)
  k += 1

for i in range(k):
  stars = get_stars(stars)
for i in stars:
  print(i)