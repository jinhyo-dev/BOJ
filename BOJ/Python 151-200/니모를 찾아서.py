while True:
  str = input()
  if str == 'EOI':
    break
  print("Found" if 'nemo' in str.lower() else "Missing")