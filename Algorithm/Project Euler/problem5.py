num = 1

while num > 0:
    for i in range(1, 21):
        if num % i != 0:
            num += 1
            break
    else:
        print(num)
        num = 0
