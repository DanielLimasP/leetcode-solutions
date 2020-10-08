def search_range(nums, target):
    left_index = extreme_insertion_index(nums, target, True)
    if left_index == len(nums) or nums[left_index] != target:
        return [-1, -1]
    return [left_index, extreme_insertion_index(nums, target, False)-1]

def extreme_insertion_index(nums, target, left):
    # Low and high index
    lo = 0
    hi = len(nums)-1

    # While lo is less than high (remember that the array is sorted)
    # The first time we call this method, it finds the leftmost index
    # The second time we call this method, lo and hi end up being the same
    # One index ahead of the rightmost element, that is the reason
    # Why we end up subtracting one.
    while lo < hi:
        # We create a new middle index
        mid = (lo + hi) // 2
        # If left flag is true, we will find the leftmost index
        if nums[mid] > target or (left and target == nums[mid]):
            hi = mid
        else: 
            lo = mid + 1
    return lo

if __name__ == "__main__": 
    test_nums = [1,1,2,3,4,5,6,7,8]
    target = 1
    print(search_range(test_nums, target))