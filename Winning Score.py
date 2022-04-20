Apple = [int(input()) for _ in range(3)]
Banana = [int(input()) for _ in range(3)]

Apple[0] *= 3
Banana[0] *=3

Apple[1] *= 2
Banana[1] *=2

if sum(Apple) == sum(Banana):
    print('T')
else:
    print('A' if sum(Apple) > sum(Banana) else 'B')