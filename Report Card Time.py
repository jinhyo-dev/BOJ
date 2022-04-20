arr = []
for _ in range(int(input())):
    name, grade = input().split()
    arr.append([name, int(grade)])

for i in range(len(arr)):
    if arr[i][1] >= 97: arr[i][1] = 'A+'
    elif arr[i][1] >= 90: arr[i][1] = 'A'
    elif arr[i][1] >= 87: arr[i][1] = 'B+'
    elif arr[i][1] >= 80: arr[i][1] = 'B'
    elif arr[i][1] >= 77: arr[i][1] = 'C+'
    elif arr[i][1] >= 70: arr[i][1] = 'C'
    elif arr[i][1] >= 67: arr[i][1] = 'D+'
    elif arr[i][1] >= 60: arr[i][1] = 'D'
    else: arr[i][1] = 'F'
    print(arr[i][0], arr[i][1])