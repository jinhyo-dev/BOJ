from collections import deque
s = deque()

while True:
  string = input()
  if string == '고무오리 디버깅 끝':
    break
  elif string == '문제':
    s.append(1)
  elif string == '고무오리':
    if s:
      s.pop()
    else:
      s.append(1)
      s.append(1)

print('힝구' if s else '고무오리야 사랑해')
