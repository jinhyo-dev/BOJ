import sys
input = sys.stdin.readline
dic = dict()
for _ in range(int(input())):
    name, isInCompany = input().split()
    if isInCompany == 'enter':
        dic[name] = 1
    else:
        del dic[name]
sorted_dic = sorted(dic.keys(), reverse=True)
print(*sorted_dic, sep='\n')