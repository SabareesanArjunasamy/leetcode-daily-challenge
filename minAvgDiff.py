import math
from typing import List


def minimumAverageDifference(self, nums: List[int]) -> int:
    l = [-1]*len(nums)
    r = [-1]*len(nums)

    def rightmean(i):
        if i == 0:
            r[i] = sum(nums[i+1:])
        elif i == len(nums)-1:
            r[i] = 0
        else:
            r[i] = r[i-1] - nums[i]

    def leftmean(i):
        if i == 0:
            l[i] = nums[i]
        else:
            l[i] = l[i-1] + nums[i]

    def average(i):
        la = l[i] // (i+1)
        ra = r[i] // (len(nums)-i-1) if (len(nums)-i-1) != 0 else 0
        avg = abs(la - ra)
        return avg

    for i in range(len(nums)):
        rightmean(i)
        leftmean(i)
    res = 0
    minavg = math.inf
    for i in range(len(nums)):
        avg = average(i)
        if avg < minavg:
            minavg = avg
            res = i
    return res
