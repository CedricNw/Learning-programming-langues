from typing import List

def majorityElement(nums: List[int]) -> int:
    if len(nums) == 0: return None
    
    dic = {}
    
    for i in nums:
        dic[i] = dic.get(i, 0) + 1
    
    for key, value in dic.items():
        if value == max(dic.values()):
            return key

print(majorityElement([2,2,1,1,1,2,2,3]))