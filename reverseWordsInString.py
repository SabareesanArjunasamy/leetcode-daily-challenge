def reverseWords(s) -> str:
    stringList = s.split()
    finalString = ''
    for i in stringList:
        finalString += i[::-1]
        finalString += ' '
    return finalString.strip()


s = "Let's take LeetCode contest"
print(reverseWords(s))
s = "Gods Ding"
print(reverseWords(s))
