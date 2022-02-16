N = int(input())
print(int(N * 0.78), end=' ')
tmp = N * 0.8
N -= N * 0.8
print(int(N * 0.78 + tmp))