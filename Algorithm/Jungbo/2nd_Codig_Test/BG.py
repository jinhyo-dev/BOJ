n = int(input())

while True:
  while n >= 5000:
    print('골드회원')
    n = -1
    break
  while n >= 3000:
    print('실버회원')
    n = -1
    break
  while n >= 1000:
    print('브론즈회원')
    n = -1
    break
  while n >= 0:
    print('일반회원')
    n = -1
    break
  while n < 0:
    break
  break
