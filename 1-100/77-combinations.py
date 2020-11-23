import logging

logging.basicConfig(filename='logs.txt', level=logging.DEBUG, format='%(asctime)s -  %(levelname)s -  %(message)s')

def combinations(n, k):
    logging.debug('START OF PROGRAM')
    res = []
    dfs(list(range(1, n+1)), k, [], res)
    return res

def dfs(nums, k, path, res):
    logging.debug("nums: {}".format(nums))
    logging.debug("k: {}".format(k))
    logging.debug("path: {}".format(path))
    logging.debug("res: {}".format(res))
    logging.debug("----------------------------------------------------")
    if len(path) == k:
        res.append(path)
        return 
    for i in range(len(nums)):
        dfs(nums[i+1:], k, path+[nums[i]], res)

if __name__ == "__main__":
    print(combinations(4, 2))