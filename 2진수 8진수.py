n = int(input(), 2)
answer = list(str(oct(n)))
answer[0] = answer[1] = ''
print(''.join(answer))
