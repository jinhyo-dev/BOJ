for _ in range(int(input())):
	arr = [0]*10
	for i in input(): arr[ord(i)-48] = 1
	print(arr.count(1))