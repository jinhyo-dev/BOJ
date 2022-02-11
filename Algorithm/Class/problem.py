import random

def find_missing(S) :
  n = len(S) + 1
  return (n**2 + n) // 2 - sum(S)

N = int(input("자연수를 입력하세요 : "))
nums = [i for i in range (1,  N + 1)]
S = random.sample(nums, len(nums) - 1)
print(S)

missing = find_missing(S);
print(missing)
