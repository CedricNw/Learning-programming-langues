def lengthOfLongestSubstring(s: str):
    solution = ""
    for i in range(len(s)):
        temp = ""
        for letter in s[i:]:
            if letter in temp:
                break
            temp += letter
            if len(temp) > len(solution):
                solution = temp

    return len(solution)

print(lengthOfLongestSubstring("pwwkew"))