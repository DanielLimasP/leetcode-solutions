def solution_problem_33(nums, target):
    #nums.sort()
    print(best_solution(nums, target))

def best_solution(nums, target):
    l, r = 0, len(nums)-1
    while l < r:
        m = l + (r-l)//2
        print(m)
        if (nums[m] >= nums[l] and (target < nums[l] or target > nums[m])) or (nums[m] < nums[l] and target <= nums[r] and target > nums[m]):
            l = m+1
        else:
            r = m
    return l if nums[l] == target else -1

# Two indices approach
def other_binary_search(nums, target):
    left = 0
    right = len(nums) - 1 

    while left <= right:
        mid = (left + right) // 2
        print("index: {} number: {}".format(mid, nums[mid]))
        print(nums)
        if target == nums[mid]:
            print(mid)
            return mid
        if nums[left] <= nums[mid]:
            if target > nums[mid] or target < nums[left]:
                left = mid + 1
            else: 
                r = mid - 1
        else: 
            if target < nums[mid] or target > nums[right]:
                r = mid - 1
            else: 
                left = mid + 1
    return -1

# This definitely is binary search, though it doesn't work properly...
def binary_search(nums, target):
    middle = nums[len(nums)//2]
    aux_nums = []
    print(middle)
    print(nums)
    if target == middle:
        print(middle)
        return middle
    else:
        if target < middle:
            aux_nums = nums[:middle]
            return binary_search(aux_nums, target)
        else:
            aux_nums = nums[middle:]
            return binary_search(aux_nums, target)
    
if __name__ == "__main__": 
    # Sorted = [0,1,2,4,5,6,7]
    test_nums = [4,5,6,7,0,1,2]
    answer = solution_problem_33(test_nums, 1)
    print(answer)
    