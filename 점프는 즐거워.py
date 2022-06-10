while True:
  try:
    arr = list(map(int, input().split()))
    N = arr[0]
    del arr[0]
    flag = True
    check = [False] * 3000

    for i in range(N - 1):
      tmp = abs(arr[i] - arr[i + 1])
      if not tmp or tmp >= N or check[tmp]:
        flag = False
        break
    print('Jolly' if flag else 'Not jolly')
  except:
    break