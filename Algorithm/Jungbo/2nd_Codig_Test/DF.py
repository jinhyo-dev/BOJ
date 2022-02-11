def fib(n):
  if n is 1:
    return 1
  elif n is 2:
    return 1
  return fib(n-1) + fib(n-2)

n = int(input())
print(fib(n))