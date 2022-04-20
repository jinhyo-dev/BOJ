def GCD(X,Y):
  while(Y): 
    X, Y = Y, X%Y
  return X

def LCM(X,Y):
  result = (X*Y) // GCD(X,Y)
  return result

for _ in range(int(input())):
  N, M = map(int, input().split())
  print(LCM(N, M), GCD(N, M))