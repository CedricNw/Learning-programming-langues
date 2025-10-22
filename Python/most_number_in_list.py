# return the number which appears the most in a given list

def get_modus_of_list(numbers: list[int]) -> int:
    dic = {}
    for num in numbers:
        dic[num] = dic.get(num, 0) + 1
        
    for name, age in dic.items():
        if age == max(dic):
            return name

print(get_modus_of_list([2,2,2,3,3,4,2]))