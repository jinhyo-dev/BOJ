from statistics import mean
arr = [int(input()) for _ in range(5)]
arr.sort()
print(int(mean(arr)), arr[2], sep='\n')