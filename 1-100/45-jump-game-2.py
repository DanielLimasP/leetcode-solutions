
from queue import deque

# https://leetcode.com/problems/jump-game-ii/discuss/899105/Python-BFS-Solution
def jump_game_2(nums):
    n = len(nums)
    visited = {}
    deq = deque([(0, nums[0], 0)])

    while deq:
        print(deq)
        index, limit, step = deq.popleft()
        if index == n-1:
            return step
        for i in range(min(index + limit, n-1), index, -1):
            if i in visited:
                continue
            if  i == n-1:
                return step+1
            deq.append([i, nums[i], step+1])
            visited[i] = True

    return -1

if __name__ == "__main__":
    print(jump_game_2([2,3,1,1,4]))