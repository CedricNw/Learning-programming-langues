# Search threw a list the libst should contain all numbers from 1 to n, but one number is missing. Find that number

def find_missing_number_in_numbers(numbers: list) -> int:
    for i in range(1, len(numbers)+1):
        if i in numbers:
            continue
        else:
            return i

def find_missing_number_via_sum_formula(numbers: list) -> int:
    n = len(numbers) + 1
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(numbers)
    return expected_sum - actual_sum

print(find_missing_number_in_numbers([1,2,3,4,7,8,6,9]))
print(find_missing_number_via_sum_formula([1,2,3,4,7,8,6,9]))