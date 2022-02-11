birth_list = []
for _ in range(int(input())):
  name, day, month, year = input().split()
  birth_list.append([int(year), int(month), int(day), name])
  birth_list.sort()

print(birth_list[-1][3])
print(birth_list[0][3])
