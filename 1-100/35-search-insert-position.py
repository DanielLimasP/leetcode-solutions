def search_insert_position(nums, target):
    print("nums: {}".format(nums))
    print("target: {}".format(target))
    lo = 0 
    hi = len(nums)-1

    while lo <= hi:
        mid = (lo + hi) // 2
        print("""
        lo: {}
        hi: {}
        mid: {}
        """.format(lo, hi, mid))

        if nums[mid] == target:
            return mid
        elif target < nums[mid]:
            hi = mid - 1
        else:
            lo = mid + 1

    return lo

if __name__ == "__main__":
    test_nums = [1,2,3,4,9,10,11,12]
    #test_nums = [1,3,5,6]
    #test_nums = [1,3]
    test_nums1 = [1,3,4,5,6]
    target = 7
    print(search_insert_position(test_nums1, target))