from typing import List

def findMaxConsecutiveOnes(nums: List[int]) -> int:
        res = cur = 0

        for n in nums:
            if n:
                cur += 1
                if cur > res:
                    res = cur
            else:
                cur = 0
        return res
    
print(findMaxConsecutiveOnes([1,1,0,1,1,1]))