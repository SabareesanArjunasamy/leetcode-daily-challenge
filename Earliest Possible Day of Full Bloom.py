class Solution:
    def earliestFullBloom(self, pt, gt) -> int:
        pairs=[]
        for i in range(len(pt)):
            pairs.append([pt[i],gt[i]])
        pairs.sort(key=lambda x:-x[1])
        maxtime=0
        currenttime=0
        for a in pairs:
            currenttime+=a[0]
            maxtime=max(maxtime,currenttime+a[1])
        return maxtime