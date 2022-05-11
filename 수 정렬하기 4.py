from sys import stdin
input = stdin.readline
arr = [int(input()) for _ in range(int(input()))]
arr.sort(reverse=True)
print(*arr, sep='\n')