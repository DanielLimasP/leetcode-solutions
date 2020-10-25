def permute(nums):
        res = []
        dfs(nums, [], res)
        return res

def dfs(nums, path, res):
    if not nums:
        res.append(path)
        return # backtracking
    for i in range(len(nums)):
        dfs(nums[:i]+nums[i+1:], path+[nums[i]], res)

if __name__ == "__main__":
    print(permute([1, 2, 3]))
    