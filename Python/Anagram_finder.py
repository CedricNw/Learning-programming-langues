# Write a function that checks if a String is an anagram

def is_anagram(first_word: str, second_word: str) -> bool:
    dic_word_one = get_letters_as_dictionary(first_word.lower())
    dic_word_two = get_letters_as_dictionary(second_word.lower())

    return dic_word_one == dic_word_two

def get_letters_as_dictionary(word: str) -> dict:
    dic = {}
    for letter in word:
        dic[letter] = dic.get(letter, 0) + 1

    return dic

print(is_anagram("Shaco", "Chaos"))