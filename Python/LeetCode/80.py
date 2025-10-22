from typing import List

def removeDuplicates(nums: List[int]) -> int:
    
    count = 1
    j = 0
    for i in range(1, len(nums)):
        if nums[i] != nums[j]:
            j += 1
            nums[j] = nums[i]
            count = 1
            
        elif count == 1:
            count += 1
            j += 1
            nums[j] = nums[i]
    return j + 1

print(removeDuplicates([1,1,1,1,2,2,3]))