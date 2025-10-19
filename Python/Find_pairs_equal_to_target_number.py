# Write a function that retruns a list with tuples that contain 2 numbers adding up to the target number

def find_pairs(numbers: list, target_number: int) -> list:
    result = set()
    
    for i in range(len(numbers)):
        
        # j start 1 after i, no list[0] with list[0] possible
        for j in range(i + 1, len(numbers)):
            
            if numbers[i] + numbers[j] == target_number:
                
                # sorted tuples (2,8) and (8,2) are the same for the set now so it gets removed
                result.add(tuple(sorted((numbers[i], numbers[j]))))
                    
    return list(result)

print(find_pairs([2, 4, 3, 5, 7, 8, 9], 10))