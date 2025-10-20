# Check if a phrase is an palimdrom (If it is read forward it says the same as backward)

def is_palimdrom(phrase: str) -> bool:
    phrase_as_arr = []
    phrase = phrase.replace(" ", "")
    for letter in phrase.lower():
        phrase_as_arr += letter
        
    arr_backwards = phrase_as_arr[::-1]
    return phrase_as_arr == arr_backwards
    
    
print(is_palimdrom("A man a plan a canal Panama"))