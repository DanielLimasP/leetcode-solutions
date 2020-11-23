#https://leetcode.com/problems/word-search/discuss/27665/Python-simple-dfs-solution
def search_word(board, word):
    if not word:
        return True
    if not board:
        return False

    for i in range(len(board)):
        for j in range(len(board[0])):
            if exist_helper(board, word, i, j):
                return True

def exist_helper(board, word, i, j):
    print(word)
    if board[i][j] == word[0]:
        if not word[1:]:
            return True

        board[i][j] = " "

        if i > 0 and exist_helper(board, word[1:], i-1, j):
            return True
        if i < len(board)-1 and exist_helper(board, word[1:], i+1, j):
            return True
        if j > 0 and exist_helper(board, word[1:], i, j-1):
            return True
        if j < len(board[0])-1 and exist_helper(board, word[1:], i, j+1):
            return True

        board[i][j] = word[0]
        return False

    else:
        return False

if __name__ == "__main__":
    print(search_word([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED"))