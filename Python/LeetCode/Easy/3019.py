from typing import List

def countKeyChanges(s: str) -> int:
    counter = 0
    old_char = s.lower()[0]
    
    for letter in s.lower()[1:]:
            if old_char != letter:
                counter += 1
                old_char = letter
                
    return counter

print(countKeyChanges("abb"))