F = {0: 0, 1: 1}
tmp = int()


def fib(n):
    if n not in F:
        F[n] = fib(n-1) + fib(n-2)
    return F[n]
    # if fib(n) <= 4000000:
    #     break;


for n in range(5000):
    if len(str(fib(n))) == 1000:
        print(n)
        break
