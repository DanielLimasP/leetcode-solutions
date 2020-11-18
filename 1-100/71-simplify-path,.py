# https://leetcode.com/problems/simplify-path/discuss/25691/9-lines-of-Python-code
def simplify_path(path):
    stack = []
    # split the given path in / and loop through the result
    for p in path.split("/"):
        if p == "..":
            # Pop the last element from the stack like this
            stack = stack[:-1]
        elif p and p != ".":
            stack.append(p)
        
    # return the first / + the stack joined by "/"
    return "/" + "/".join(stack)

if __name__ == "__main__":
    simplify_path("/a/./b/../../c")