N = int(input())
if N == 1: print('*')
else:
    for i in range(N):
        print('* ' * N if i % 2 == 0 else ' *' * N)