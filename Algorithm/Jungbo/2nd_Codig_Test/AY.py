time, pay = map(int, input().split())

if time > 40:
  pay = 40 * pay + (time - 40) * pay * 1.5
  print(int(pay))
else:
  print(int(time*pay))