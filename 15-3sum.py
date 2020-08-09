#https://www.youtube.com/watch?v=erEHQO0xljc
def threeSum(nums):
    nums.sort()
    
    triplets = []

    for i in range(len(nums)-2):

        if i > 0 and nums[i] == nums[i-1]:
            continue

        left = i+1
        right = len(nums)-1

        while left < right:
            currSum = nums[i] + nums[left] + nums[right]
            if currSum == 0:
                triplets.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1

                while left < right and nums[left] == nums[right]:
                    left += 1
                while left < right and nums[right] == nums[left]:
                    right -= 1

            elif currSum < 0: 
                left += 1
            else:
                right -= 1
    return triplets

print(threeSum([-4, -1, -1, 0, 1, 2]))