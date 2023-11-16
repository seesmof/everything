"""
кінь
дах
атом
вулиця
хвіст
бавовна
вівця
плакат
зоопарк
стіл
"""


def longestConsecutive(nums):
    nums = sorted(nums)

    for i in range(len(nums)):
        r = list(range(min(nums), max(nums) + 1))
        if set(r).issubset(set(nums)):
            return len(r)
        else:
            nums = nums[:-1]


nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
res = longestConsecutive(nums)
print(res, res == 9)

nums = [100, 4, 200, 1, 3, 2]
res = longestConsecutive(nums)
print(res, res == 4)

print(len([]))
