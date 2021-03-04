def remove_duplicates_2(nums):
    tail = 0
    for n in nums:
        if tail < 0 or n > nums[tail-2]:
            nums[tail] = n
            tail += 1
    return tail

if __name__ == "__main__":
    print(remove_duplicates_2([1, 1, 1, 2, 2, 3]))