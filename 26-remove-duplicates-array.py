def removeDuplicates(nums):
    i = 0
    while i < len(nums) - 1:
        if nums[i] == nums[i + 1]:
            del nums[i]
        else:
            i += 1
    return len(nums)


if __name__ == '__main__':
    print(removeDuplicates([1, 1, 2, 3, 3, 4, 5, 5]))
