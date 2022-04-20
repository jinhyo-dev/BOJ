X, Y = input().split()
X = X[::-1]
Y = Y[::-1]
print(int(str(int(X) + int(Y))[::-1]))