arr = [int(input()) for _ in range(int(input()))]
bool = True
for i in range(1, len(arr)):
    if arr[i] > arr[0]:
        bool = False
print('S' if bool == True else 'N')