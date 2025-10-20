# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.
from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    dic = {}
    i = 0
    for num in nums: 
        searched_number = target - num
        if searched_number in dic:
            return [dic[searched_number], i]
        dic[num] = i
        i += 1
    return

print(twoSum([1,2,3,7,5], 10))