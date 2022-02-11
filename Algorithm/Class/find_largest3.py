import random

def find_largest(nums) :
  if len(nums) ==1:
    return nums[0]
  else:
    mid = len(nums) // 2
    left = find_largest(nums[:mid])
    right = find_largest(nums[mid:])
    return left if left > right else right 
    


sequence = list(range(10, 100))
N = 10 
nums = random.sample(sequence, N)
MAX = find_largest(nums);
print(nums)
print(MAX , max(nums))