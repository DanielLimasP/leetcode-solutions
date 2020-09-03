def validParentheses(s):
    stack = []
    mapping = {"(":")", "{":"}", "[":"]"}
    open_par = set(["(", "[", "{"])
    for c in s:
        if c in open_par:
            stack.append(c)
        # If stack exists and current par == top element
        elif stack and c == mapping[stack[-1]]:
            stack.pop()
        else:
            return False
    return stack == []

print(validParentheses("(){}[]"))
print(validParentheses("(){["))
print(validParentheses("{}[)"))

    