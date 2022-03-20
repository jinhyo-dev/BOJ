arr = [int(input()) for _ in range(3)]
arr[1] *= 2
arr[2] *= 3
print('happy' if sum(arr) >= 10 else 'sad')