n = int(input())

if n % 4 == 0 and n % 100 != 0 or n % 400 == 0:
  print("{}년은 윤년입니다".format(n))
else:
  print('{}년은 윤년이 아닙니다'.format(n))
