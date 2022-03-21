N = int(input())
arr = list(map(int, input().split()))
print('yes' if sum(arr) % 3 == 0 else 'no')