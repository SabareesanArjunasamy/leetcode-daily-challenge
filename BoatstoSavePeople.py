class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        lo, hi, ans = 0, len(people) - 1, 0
        while lo <= hi:
            if people[hi] + people[lo] <= limit: lo += 1
            hi -= 1; ans += 1
        return ans