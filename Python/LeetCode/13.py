# Write a function that turns a roman number into an integer

def roman_to_integer(roman: str) -> int:
    
    dic = {
        "I": 1,
        "IV": 4,
        "V": 5,
        "IX": 9,
        "X": 10,
        "XL": 40,
        "L": 50,
        "XC": 90,
        "C": 100,
        "CD": 400,
        "D": 500,
        "CM": 900,
        "M": 1000
    }
    
    result = 0
    
    for i in range(len(roman)-1):
        if dic[roman[i]] < dic[roman[i+1]]:
            
            result += dic[roman[i] + roman[i+1]]
            if dic[roman[i] + roman[i+1]] == dic[roman[-1]]:
                return result
        else:
            result += dic[roman[i]]
            
    result += dic[roman[-1]]
    
    return result

print(roman_to_integer("MMMCMX"))