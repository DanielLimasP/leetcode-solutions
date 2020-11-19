def combine(n, k):
    res = []
    nums = []
    
    for i in range(1, n+1):
        nums.append(i)
        
    dfs(nums, k, 0, [], res)
    return res
    
def dfs(nums, k, index, path, res):
    if k == 0:
        res.append(path)
        return 
    for i in range(index, len(nums)):
        dfs(nums, k-1, index+1, path+[nums[i]], res)


if __name__ == "__main__":
    print(combine(4, 2))
    