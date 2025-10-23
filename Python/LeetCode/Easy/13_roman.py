# Write a function that turns a roman number into an integer

def roman_to_integer(roman: str) -> int:
    
    if not roman:
        return 0
    
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
    old_letter = ""
    
    for i in range(0, len(roman)):

        if old_letter == "":
            old_letter = roman[i]
        
        else:
            if dic.get(old_letter) < dic[roman[i]]:
                result += dic.get(old_letter + roman[i])
                old_letter = ""
                if i == len(roman)-1:
                    return result
            else:
                result += dic.get(old_letter)
                old_letter = roman[i]
                
        if i == len(roman)-1:
            print("Jdiwa")
            result += dic.get(roman[i])
        
    return result

print(roman_to_integer("MDCXCV"))