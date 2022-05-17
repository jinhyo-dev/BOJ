w = [int(input()) for _ in range(5)]
X, Y = w[0] * w[4], w[1]
if w[4] > w[2]:
    Y += (w[4] - w[2]) * w[3]
print(X if X < Y else Y)