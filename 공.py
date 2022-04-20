M = int(input())
ball = [1, 2, 3]
for _ in range(M):
    X, Y = map(int, input().split())
    xi = ball.index(X)
    yi = ball.index(Y)
    ball[xi], ball[yi] = ball[yi], ball[xi]
print(ball[0])