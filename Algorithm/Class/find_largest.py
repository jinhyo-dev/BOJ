import random

def find_largest(nums) :
  if len(nums) == 1:
    return nums[0]
  else :
    largest = find_largest(nums[1:])
    if nums[0] < largest:
      return largest
    else :
      return nums[0]

sequence = list(range(10, 100))
N = 10 
nums = random.sample(sequence, N)
MAX = find_largest(nums);
print(nums)
print(MAX , max(nums))