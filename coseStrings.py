import collections


def closeStrings(word1: str, word2: str) -> bool:
    c1 = collections.Counter(word1)
    c2 = collections.Counter(word2)
    set1 = set(word1)
    set2 = set(word2)
    s1 = sorted(c1.values())
    s2 = sorted(c2.values())
    return s1 == s2 and set1 == set2
