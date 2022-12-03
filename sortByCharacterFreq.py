from collections import Counter


def sortByCharFreq(s: str):
    sortedString = sorted(s)
    counter = Counter(sortedString)
    res = ''

    sortedCharsByFreq = counter.most_common()

    for char, freq in sortedCharsByFreq:
        res += char * freq
    return res


choise = 'y'
while choise == 'y':
    string = input('Please enter the Strin to sort by charecter freq : ')
    print(sortByCharFreq(string))
    choise = input('Would you like to continue y/n : ')
