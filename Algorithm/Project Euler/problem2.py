# def fib(n):
#     if n <= 1:
#         return n
#     else:
#         a, b = 0, 1
#         for i in range(2, n+1):
#             a, b = b, a+b
#         return b


# for n in range(100001):
#     print(n, ":", fib(n))

F = {0: 0, 1: 1}
tmp = int()


def fib(n):
    if n not in F:
        F[n] = fib(n-1) + fib(n-2)
    return F[n]
    # if fib(n) <= 4000000:
    #     break;


for n in range(101):
    if fib(n) <= 4000000:
        if fib(n) % 2 == 0:
            tmp += fib(n)
            print(n, ":", fib(n))

print("The answer is : ", tmp)
# print(n, ":", fib(n))
