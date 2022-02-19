for _ in range(int(input())):
    N, M = map(int, input().split())
    tmp = list(map(int, input().split()))
    q = []
    arr = []
    for i in range(N):
        q.append([tmp[i], i])
    while len(q):
        if q[0][0] == max(q)[0]:
            arr.append(q[0])
            del q[0]
        else:
            q.append(q[0])
            del q[0]

    for i in range(N):
        if arr[i][1] == M:
            print(i+1)
            break