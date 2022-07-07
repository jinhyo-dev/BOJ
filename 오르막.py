arr = list(map(int, input().split()))
compare = sorted(arr)
print('Good' if arr == compare else 'Bad')
