def halvesAreAlike(s: str) -> bool:
    vowels = set('aeiouAEIOU')
    a, b = 0, 0
    for i in range(len(s)//2):
        if s[i] in vowels:
            a += 1
        if s[-i-1] in vowels:
            b += 1
    return a == b
