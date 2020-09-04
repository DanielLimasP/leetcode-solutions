# Backtracking solution
def generateParentheses(n):
    answer = []
    def backtrack(s = '', left = 0, right = 0):
        print(s)
        if len(s) == 2 * n:
            answer.append(s)
            return
        if left < n:
            backtrack(s+'(', left+1, right)
        if right < left:
            backtrack(s+')', left, right+1)
    backtrack()
    return answer

print(generateParentheses(2))