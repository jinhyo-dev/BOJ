x, y, w, s = map(int, input().split())
m1 = (x + y) * w

if (x + y) % 2:
    m2 = (max(x, y) - 1) * s + w
else:
    m2 = max(x, y) * s
m3 = (min(x, y) * s) + (abs(x - y) * w)

print(min(m1, m2, m3))