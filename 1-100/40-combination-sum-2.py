# Kudos to this guy:
# https://www.youtube.com/watch?v=IER1ducXujU&ab_channel=KevinNaughtonJr.

def combination_sum_2(candidates, target):
    res = []
    candidates.sort()
    dfs(candidates, target, 0, [], res)
    return res
    
def dfs(candidates, target, index, path, res):
    if target < 0:
        return  # backtracking
    if target == 0:
        res.append(path)
        return  # backtracking 
    for i in range(index, len(candidates)):
        if i > index and candidates[i] == candidates[i-1]:
            continue
        dfs(candidates, target-candidates[i], i+1, path+[candidates[i]], res)

if __name__ =="__main__":
    print(combination_sum_2([10,1,2,7,6,1,5], 8))