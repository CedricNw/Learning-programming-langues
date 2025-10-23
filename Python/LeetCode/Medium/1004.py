from typing import List

def longestOnes(nums: List[int], k: int) -> int:
        
    res = 0
    left = 0
    zeros = 0

    for right in range(len(nums)):
        if nums[right] == 0:
            zeros += 1

        # Wenn zu viele Nullen im Fenster, linkes Ende verschieben
        while zeros > k:
            if nums[left] == 0:
                zeros -= 1
            left += 1

        # Fensterlänge aktualisieren
        res = max(res, right - left + 1)

    return res

print(longestOnes(nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2))
