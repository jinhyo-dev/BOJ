def lpf(x):
    lpf = 2
    while (x > lpf):
        if (x % lpf == 0):
            x = x/lpf
        else:
            lpf += 1
    return x


print(lpf(600851475143))
