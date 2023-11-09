def mooveToBack(nums, index):
    for i in range(index, len(nums) - 1):
        tmp = -1
        nums[i] = nums[i + 1]
        nums[i + 1] = tmp
    return nums


def removeDups(nums, met):
    for _, el in enumerate(nums):
        met[el] = 0

    for i in range(len(nums)):
        element = nums[i]

        if element == -1:
            continue
        elif met[element] > 0:
            mooveToBack(nums, i)
        else:
            met[element] += 1


def removeDuplicates(nums: [int]) -> int:
    neededSize = len(set(nums))
    met = {}
    res = 0

        removeDups(nums, met)

    for _ in range(len(nums) - neededSize):
        nums.pop()

    res = len(nums)
    return res


arr = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
res = removeDuplicates(arr)
print(arr)
