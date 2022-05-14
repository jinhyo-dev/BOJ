for _ in range(int(input())):
  string = input().split()
  for w in string:
    print(w[::-1], end=' ')
  print()