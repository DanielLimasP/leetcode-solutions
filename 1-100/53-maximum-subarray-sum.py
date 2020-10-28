# https://hackernoon.com/kadanes-algorithm-explained-50316f4fd8a6
# Remember Kadane's algorithm
def maximum_subarray(nums):
    curr_max = float("-inf")
    total_max = float("-inf")    

    for n in nums:
        curr_max = max(curr_max, 0) + n
        total_max = max(total_max, curr_max)
    
    return total_max

if __name__ == "__main__": 
    print(maximum_subarray([-2,1,-3,4,-1,2,1,-5,4]))