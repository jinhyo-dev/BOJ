burgers = [int(input()) for _ in range(3)]
drinks = [int(input()) for _ in range(2)]
burgers.sort(), drinks.sort()
print(burgers[0] + drinks[0] - 50)