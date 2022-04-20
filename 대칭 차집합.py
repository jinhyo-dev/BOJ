A, B = map(int, input().split())
A_arr = set(map(int, input().split()))
B_arr = set(map(int, input().split()))
print(len(A_arr - B_arr) + len(B_arr - A_arr))