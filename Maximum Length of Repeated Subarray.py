def findLength(nums1, nums2):
    maxLength = 0
    dp = [[0] * (len(nums2)+1) for _ in range(len(nums1)+1)]
    for i in range(len(nums1)):
        for j in range(len(nums2)):
            if nums1[i] == nums2[j]:
                currentLength = dp[i][j] + 1
                dp[i+1][j+1] = currentLength
                maxLength = max(maxLength, currentLength)
                print(dp, sep='\n')
    return maxLength


nums1 = [1, 2, 3, 2, 1]
nums2 = [3, 2, 1, 4, 7]

print(findLength(nums1, nums2))

nums1 = [0, 0, 0, 0, 0]
nums2 = [0, 0, 0, 0, 0]

print(findLength(nums1, nums2))
