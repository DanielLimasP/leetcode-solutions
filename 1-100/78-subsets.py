def subsets(nums):
    res = []
    dfs(sorted(nums), 0, [], res)
    return res

def dfs(nums, index, path, res):
    res.append(path)
    for i in range(index, len(nums)):
        dfs(nums, index+1, path+[nums[i]], res)

if __name__ == "__main__":
    print(subsets([1, 2, 3]))