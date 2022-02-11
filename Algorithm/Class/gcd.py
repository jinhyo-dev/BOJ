import math


def divisors(N):
    divs = []
    for i in range(1, int(math.sqrt(N) + 1)):
        if N % i == 0:
            divs.append(i)
            divs.append(N // i)
    return sorted(divs)


N = int(input("정수를 입력하세요 : "))
M = int(input("정수를 입력하세요 : "))
div1 = divisors(N)
div2 = divisors(M)

for d in div1:
    if d in div2:
        print(d)
