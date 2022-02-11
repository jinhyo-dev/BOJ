from itertools import permutations

word1,word2,word3 = input("복면산 입력해라 : ").split()

letters = sorted(set(word1+word2+word3))
digits = list(range(10))
print(letters, digits)

def to_int(word, dic):
    value = 0
    rev = word[::-1]
    for i in range(len(rev)):
        value += dic[rev[i]] * (10**i)

    return value

perms = list(permutations(digits,len(letters)))
for perm in perms:
    dic = {k:v for k, v in zip(letters, perm)}
    if dic[word1[0]]==0 or dic[word2[0]]==0 or dic[word3[0]]==0:
        continue
    a = to_int(word1,dic)
    b = to_int(word2,dic)
    c = to_int(word3,dic)
    if a+b==c:
        print(dic)