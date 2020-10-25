def permutations_2(nums):
    result = []
    dfs(nums, [], result)
    return result

def dfs(nums, path, result):
    if not nums and path not in result:
        result.append(path)
        return
    for i in range(len(nums)):
        dfs(nums[:i]+nums[i+1:], path+[nums[i]], result)

if __name__ == "__main__":
    print(permutations_2([1, 1, 2]))