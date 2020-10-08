# This is a general solution for K-sum of numbers that add up to target
# Problem proved to be way to hard. Generic solution is too complicated
def fourSum(nums, target):
    def ksum(start, k, target):
        res = []
        # This sentence here is validation to see wheter or not the numbers 
        # in the array add up to the target
        if len(nums) == 0 or nums[0] * k > target or target > nums[-1] * k:
            return res
        # if k is already equal to two...
        if k == 2:
            return twoSum(nums, target)
        for i in range(len(nums)):
            if i == 0 or nums[i-1] != nums[i]:
                for _, set in enumerate(ksum(nums[i+1:], target-nums[i], k-1)):
                    res.append([nums[i]] + set)
        return res

    def twoSum(nums, target):
        res = []
        lo = 0
        hi = len(nums) - 1
        while(lo < hi):
            su = nums[lo] + nums[hi]
            if su < target or (lo > 0 and nums[0] == nums[lo - 1]):
                lo += 1
            elif su > target or (hi < len(nums)) - 1 and nums[hi] == nums[hi+1]:
                hi -= 1
            else:
                res.append([nums[lo], nums[hi]])
                lo += 1
                hi -= 1
            return res
    nums.sort()
    return ksum(nums, 4, target)

nums = [1, 0, -1, 0, -2, 2]
if __name__ == "__main__":
    print(fourSum(nums, 0))