def combination_sum(candidates, target, return_list):
    return_list = []
    depth_first_search(candidates, target, [], return_list)
    return return_list

def depth_first_search(nums, target, path, return_list):
    if target < 0:
        return
    if target == 0:
        return_list.append(path)
        return 
    for i in range(len(nums)):
        depth_first_search(nums[i:], target-nums[i], path+[nums[i]], return_list)

if __name__ == "__main__":
    ret = []
    print(combination_sum([2, 3, 6, 7], 7, ret))