# solved with the help of leetcode
def threeSumClosest(nums, target):
    nums.sort()
    diff = float('inf')

    for i in range(len(nums)):

        # Arbitrary choice
        left = i+1
        right = len(nums)-1

        while left < right:
            currSum = nums[i] + nums[left] + nums[right]

            if abs(currSum - target) < abs(diff):
                diff = target - currSum

            if currSum < target:
                left += 1
            else: 
                right -= 1

            if diff == 0:
                break

    return target - diff

result_2 = [-1, 2, 1, -4] # target 1
new_nums = [-1, -3, -5, 3, 2] #[-5, -3, -1, 2, 3]
print(threeSumClosest(new_nums, -8))
