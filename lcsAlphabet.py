def longestContinuousSubstring(s: str) -> int:
    ans = i = 0
    while i < len(s):
        j = i
        while j + 1 < len(s) and ord(s[j+1]) - ord(s[j]) == 1:
            j += 1
        ans = max(ans, j - i + 1)

        if i == j:
            i += 1
        else:
            i = j
    return ans


string = 'awy'
print(longestContinuousSubstring(string))
string = 'abcde'
print(longestContinuousSubstring(string))
string = 'abkxyz'
print(longestContinuousSubstring(string))
string = 'abkuhf'
print(longestContinuousSubstring(string))
