from collections import Counter

def findOriginalArray( changed):
        n = len(changed)
        freq = Counter(changed)
        changed.sort()
        if n % 2 != 0:
            return []
        result = []
        for i in changed:
            if freq[i] > 0:
                if i == 0 and freq[0] < 2:
                    return []
                if i*2 not in freq or freq[i*2] == 0:
                    return []
                freq[i] -= 1
                freq[i*2] -= 1
                result.append(i)
        return result
    
changed = [1,3,4,2,6,8]
print(findOriginalArray(changed))
changed = [6,3,0,1]
print(findOriginalArray(changed))
changed = [1]
print(findOriginalArray(changed))
