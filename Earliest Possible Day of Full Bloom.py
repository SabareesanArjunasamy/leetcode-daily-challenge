class Solution:
    def earliestFullBloom(self, pt, gt) -> int:
        pair=[]
        for i in range(len(pt)):
            pair.append([pt[i],gt[i]])
        pair.sort(key=lambda x:-x[1])
        maxtime=0
        currenttime=0
        for a in pair:
            currenttime+=a[0]
            maxtime=max(maxtime,currenttime+a[1])
        return maxtime