import sys
while True:
  parantheses = sys.stdin.readline().rstrip()
  bool = False
  stack = []
  if parantheses == '.':
    break

  for i in parantheses:
    if i == "(" or i == "[":
      stack.append(i)
    elif i == ")":
      if not stack or stack[-1] == "[":
        print("no")
        bool = True
        break
      else:
        stack.pop()
    elif i == "]":
      if not stack or stack[-1] == "(":
        print("no")
        bool = True
        break
      else:
        stack.pop()
  if bool == False:
    print("yes") if not stack else print("no")