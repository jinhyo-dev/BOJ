h, w = map(float, input().split())
avg = ((h - 100) * 0.9)

def BMI(h, w):
  bmi = (((w - avg) * 100)/ avg)
  if bmi <= 10:
    print('정상')
  elif bmi > 10 and bmi <= 20:
    print('과체중')
  else:
    print('비만')
    
BMI(h, w)