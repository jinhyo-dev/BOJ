import random

def findLargest(nums) :
  max = 0 
  for i in range (len(nums)) :
    if(max < nums[i]) :
      max = nums[i]
      return max


sequence = list(range(10, 100))
N = 10 
nums = random.sample(sequence, N)
MAX = findLargest(nums);
print(nums)
print(MAX , max(nums))