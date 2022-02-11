from itertools import permutations

words = ["A", "MERRY", "XMAS", "TO", "ALL"] 


def to_int(word, dic):
    value = 0
    rev = word[::-1]
    for i in range(len(rev)):
        value += dic[rev[i]] * (10**i)
    return value

def is_sqaure(n):
    return int(n ** 0.5) ** 2 == n

def check_sqaure(word, dic):
    n = to_int(word, dic)
    s = 0
    for i in range(len(word)):
        s += dic[word[i]]
    return is_sqaure(n) and is_sqaure(s)

def is_valid(words, dic):
    for i in range(len(words)):
        if (check_sqaure(words[i], dic)):
            return False
    return True

letters = list(set("".join(words)))
digits = list(range(10))
perms = list(permutations(digits, len(letters)))
for perm in perms:
    dic= {k:v for k, v in zip(letters, perm)}
    if is_valid(words, dic):
        print(dic)