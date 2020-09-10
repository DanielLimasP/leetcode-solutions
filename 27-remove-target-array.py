def removeTargetFromArray(nums, target):
    i = 0
    while i < len(nums):
        if nums[i] == target:
            del nums[i]
        else:
            i += 1
        print(nums)
    return len(nums)


if __name__ == "__main__":
    print(removeTargetFromArray([3, 2, 2, 3], 3))
