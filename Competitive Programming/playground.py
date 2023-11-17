def longestConsecutive(nums: [int]) -> int:
    nums = set(nums)
    longest = 0

    for num in nums:
        if num - 1 not in nums:
            length = 0
            while num + length in nums:
                length += 1
            longest = max(length, longest)

    return longest


arr = [100, 4, 200, 1, 3, 2]
res = longestConsecutive(arr)
print(res)
