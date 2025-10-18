from typing import List

def mostCommonWord(paragraph: str, banned) -> str:
    paragraph = paragraph.lower()

    words = paragraph.split(" ")
    dic = {}
    for word in words:
        word = word.replace(".", "")
        word = word.replace(",", "")
        if word in banned:
            if word in words:
                words.remove(word)
        else:
            dic[word] = dic.get(word, 0) + 1

    return max(dic, key=dic.get)

x = "Bob hit a ball, the hit BALL flew far after it was hit."

print(mostCommonWord(x, ["hit"]))