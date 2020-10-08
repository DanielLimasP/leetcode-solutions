def twoSum(nums, target):
    # We create the dictionary
    seen = {}
    # enumerate returns the 'index' and the 'num' in the list
    for index, num in enumerate(nums):
        # other is our target minus the num found in the current index
        complement = target - num
        if complement in seen:
            # If the complement of the current index is in the dictionary, return both indices
            return [seen[complement], index]
        else:
            # Else, we add the current number, in the index i to the dictionary
            seen[num] = index 
    return []

## Test code
list = [2, 7, 11, 15]
target = 9

print(twoSum(list, target))