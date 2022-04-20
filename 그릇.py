bowl = input()
bowl_list = list(bowl)
cnt = 10

for i in range(1, len(bowl_list)):
  if bowl_list[i-1] == bowl_list[i]:
    cnt += 5
  else: 
    cnt += 10
print(cnt)