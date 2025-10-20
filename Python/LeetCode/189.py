# Write a function that rotates a list by a parameter

def rotate_list(numbers: list, k: int) -> list:
    n = numbers[-k:]
    return n + numbers[0:-k]
    
print(rotate_list([1,2,3,4,5,6,7,8,9], 3))