
def binary_search(arr: list, number: int) -> int:

    left = 0
    right = len(arr) - 1

    while left <= right:
        
        mid = (left + right) // 2
                
        if arr[mid] == number:
            return mid
        
        elif arr[mid] < number:
            left = mid + 1
        else:
            right = mid -1

print(binary_search([0,1,2,3,4,5,6,7,8,9,10], 7))