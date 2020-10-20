# https://leetcode.com/problems/first-missing-positive/discuss/17080/Python-O(1)-space-O(n)-time-solution-with-explanation
# 1. for any array whose length is l, the first missing positive must be in range [1,...,l+1], 
#    so we only have to care about those elements in this range and remove the rest.
# 2. we can use the array index as the hash to restore the frequency of each number within 
#     the range [1,...,l+1] 
# After removing all the numbers greater than or equal to n, all the numbers remaining are 
# smaller than n. If any number i appears, we add n to nums[i] which makes nums[i]>=n. 
# Therefore, if nums[i]<n, it means i never appears in the array and we should return i.

def first_missing_positive(nums):
    n = len(nums)
    nums = list(set(nums)) + [0]
    for i in range(n):
        if nums[i] < 0 or nums[i] >= n:
            nums[i] = 0
    for i in range(n):
        nums[nums[i]%n] += n 
    for i in range(1, n):
        if nums[i]//n == 0:
            return i
    return n

if __name__ == "__main__":
    print(first_missing_positive([3, 4, -1, 1]))