def sumEvenAfterQueries(nums, queries):
    even_sum = sum(v for v in nums if v % 2 == 0)
    res = []
    for val, idx in queries:
        if nums[idx] % 2 == 0:
            even_sum -= nums[idx]
        nums[idx] += val
        if nums[idx] % 2 == 0:
            even_sum += nums[idx]

        res.append(even_sum)

    return res


nums = [1, 2, 3, 4]
queries = [[1, 0], [-3, 1], [-4, 0], [2, 3]]
# Output: [8,6,2,4]
print(sumEvenAfterQueries(nums, queries))

nums = [1]
queries = [[4, 0]]
# Output: [0]

print(sumEvenAfterQueries(nums, queries))
