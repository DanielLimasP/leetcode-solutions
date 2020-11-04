from queue import deque

# Leetcode won't accept this solution
# Apparently it need dynamic programmin
# because of time limit exceeded with 
# a test case.
def jump_game(nums):
    n = len(nums)
    visited = {}
    deq = deque([(0, nums[0], 0)])

    while deq:
        index, limit, step = deq.popleft()
        if index == n-1:
            return True
        for i in range(min(index + limit, n-1), index, -1):
            if i in visited:
                continue
            if i == n-1:
                return True
            deq.append([i, nums[i], step+1])
            visited[i] = True

    return False

# Greedy solution
def greedy_solution(nums):
    last_pos = len(nums)-1
    for i, n in reversed(list(enumerate(nums))):
        if i + n >= last_pos:
            last_pos = i
    return last_pos == 0

if __name__ == "__main__":
    print(jump_game([3,2,1,0,4]))
    print(greedy_solution([3,2,1,0,4]))
