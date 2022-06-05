for i in range(int(input())):
  string = list(input().split())
  print(f'Case #{i+1}: {" ".join(string[::-1])}')