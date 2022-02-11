import sys
parentheses = sys.stdin.readline().rstrip()
flag = 0
stack = []
for i in parentheses:
  if i == "(" or i == "[":
    stack.append(i)
  elif i == ")": 
    if not stack or stack[-1] == "[":
      print("불균형")
      flag = 1
      break
    else:
      stack.pop()
  elif i == "]":
    if not stack or stack[-1] == "(":
      print("불균형")
      flag = 1
      break
    else:
      stack.pop()
  
if flag == 0:
  if not stack :  
    print("균형")
  else:
    print("불균형")