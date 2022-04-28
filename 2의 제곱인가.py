N = int(input())
squares = [2**i for i in range(31)]

print(1 if N in squares else 0)