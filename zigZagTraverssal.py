def generateStartingIndices(n,m):
    indices = [(0,0)]
    while indices[-1][1]!=m:
        indices.append((0,indices[-1][1]+1))
    while indices[-1][0]!=n:
        indices.append((indices[-1][0]+1,m))
    return indices

def generatePattern(i,j):
    indices = [(i,j)]
    while indices[-1][1]!=0:
        le = indices[-1]
        indices.append((le[0]+1,le[1]-1))
    return indices
    
def zigzagTraverse(array):
    m = len(array)-1
    n = len(array[0])-1
    start_indices = generateStartingIndices(m,n)
    final_indices = []
    
    for i in range(len(start_indices)):
        e = start_indices[i]
        seq = generatePattern(e[0],e[1])
        if i%2!=0: seq.reverse()
        final_indices.extend(seq)
        
    res = []
    for e in final_indices:
        i, j = e
        if i<=m and j<=n:
            res.append(array[i][j])
    return res

matrix = [
  [1, 3, 4, 10],
  [2, 5, 9, 11],
  [6, 8, 12, 15],
  [7, 13, 14, 16]
]

x = zigzagTraverse(matrix)
print(x)
