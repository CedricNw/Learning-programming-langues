
x = [1,2,3,4,5,6,7,8,10]

def how_many_numbers_in_list(set: list):
    count = 0
    for i in set:
        if i+1 in set:
            count += 1

    return count

print(how_many_numbers_in_list(set(x)))

