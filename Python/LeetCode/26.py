from typing import List

def removeDuplicates(nums: List[int]) -> int:
    
    j = 0
    for i in range(1, len(nums)):
        if nums[i] != nums[j]:
            j += 1
            nums[j] = nums[i]
    
    print(nums)
    return j + 1
        

l = [1,1,1,2,3,4,4]
print(l[:removeDuplicates(l)])