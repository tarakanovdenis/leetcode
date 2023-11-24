# Given an integer array nums, 
# return true if any value appears 
# at least twice in the array, 
# and return false if every element is distinct.

# Example 1:
# Input: nums = [1,2,3,1]
# Output: true

# Example 2:
# Input: nums = [1,2,3,4]
# Output: false

# Example 3:
# Input: nums = [1,1,1,3,3,4,3,2,4,2]
# Output: true

from typing import List

tests = []

tests.append({'input': [1, 2, 3, 1],
              'output': True})

tests.append({'input': [1, 2, 3, 4],
              'output': False})

tests.append({'input': [1, 1, 1, 3, 3, 4, 3, 2, 4, 2],
              'output': True})


def containsDuplicate(nums: List[int]) -> bool:
    return True if len(nums) != len(set(nums)) else False
    
    # length = len(nums)
    # for i in range(0, length):
    #     for j in range(i + 1, length):
    #         if nums[i] == nums[j]:
    #             return True
    # return False
    
    # nums.sort()
    # for i in range(len(nums) - 1):
    #     if nums[i] == nums[i + 1]:
    #         return True
    # return False
    
    # d = {}
    # for idx, i in enumerate(nums):
    #     if nums[idx] in d.keys():
    #         return True
    #     d[i] = 1
    # return False
        
    # s = set()
    # for idx, i in enumerate(nums):
    #     if i in s:
    #         return True
    #     s.add(i)
    # return False
    
    # d = {}
    # for idx, i in enumerate(nums):
    #     d[i] = d.get(i, 0) + 1
    # for i in d.values():
    #     return True if i > 1 else False
        
for test in tests:
    print(containsDuplicate(test['input']) == test['output'])