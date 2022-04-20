price, num, money = map(int, input().split())
print((price * num) - money) if price * num > money else print(0)