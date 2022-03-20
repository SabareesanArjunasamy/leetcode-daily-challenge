class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        hash_map = {i:[0,0,0] for i in range(1, 7)}
        N = len(tops)
        for i in range(N):
            if tops[i] == bottoms[i]:
                hash_map[tops[i]][2] += 1
            else:
                hash_map[tops[i]][0] += 1
                hash_map[bottoms[i]][1] += 1
        res = N
        for i in range(1, 7):
            if sum(hash_map[i]) >= N:
                res = min(res, *hash_map[i][:-1])
        return -1 if res == N else res