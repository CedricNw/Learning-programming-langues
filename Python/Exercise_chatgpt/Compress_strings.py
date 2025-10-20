# Write a method that compresses a string so 'aaaabbc' => 'a4b2c', when the new string ain't shorter than return the old one

def compress_string(phrase: str) -> str:
    
    result = phrase[0]
    counter = 0
    for i in phrase:
        
        if i == result[-1]:
            counter += 1
        else:
            result += str(counter)
            counter = 1
            result += i
    result += str(counter)
    
    if len(result) < len(phrase):
        return result
    else:
        return phrase
    
print(compress_string('aaaabbc'))