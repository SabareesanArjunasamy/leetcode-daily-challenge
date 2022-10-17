def maximumScore(nums, multipliers) -> int:
        n = len(nums)
        m = len(multipliers)
        
        dp = [[0]*(m+1) for i in range(m+1)]
        for j in range(m-1,-1,-1):
            for low in range(j,-1,-1):
                first = nums [low]*multipliers[j]+dp[j+1][low+1]
                last = nums[n-1-(j-low)]*multipliers[j]+dp[j+1][low]
                dp[j][low] = max(first, last)
        return dp[0][0]
    
nums,multipliers  = [1,2,3],[3,2,1]
print(maximumScore(nums,multipliers))
# expected Output: 14
nums,multipliers2  = [-5,-3,-3,-2,7,1],[-10,-5,3,4,6]
print(maximumScore(nums,multipliers2))
# expected Output: 102
