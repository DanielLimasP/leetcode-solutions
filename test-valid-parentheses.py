def testSolution(s):
    mapping = {"(":")", "{":"}", "[":"]"}
    open_map = set(["(", "{", "["])
    stack = []

    for c in s:
        if c in open_map:
            stack.append(c)
        elif c == mapping[stack[-1]]:
            stack.pop()

    if len(stack) == 0:
        return True
    else: 
        return False

print(testSolution("[]{}()"))
print(testSolution("[]{("))
print(testSolution("[{})"))