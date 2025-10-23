# Write a function that rotates a list by a parameter

from typing import List

def rotate_list(nums: List[int], k: int) -> list:
    k = k%len(nums)
    nums[:] =  nums[-k:] + nums[0:-k]
    
    print(nums)
    
rotate_list([1,2,3,4,5,6,7], 3)