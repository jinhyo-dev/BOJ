string = list(input())
name = input()
friend = []

for i in string:
  if 65 <= ord(i) < 91:
    friend.append(i)
  elif 97 <= ord(i) < 123:
    friend.append(i)

friend = ''.join(friend)

print(1 if name in friend else 0)
