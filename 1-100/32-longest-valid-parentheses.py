# I might start commenting like this...
# longest substring of valid parentheses
def solution_prob_32(s):
    # Longest substring
    longest_sub = 0
    # We use the stack approach
    i_stack = []
    # Need to init the stack with a -1
    i_stack.append(-1)
    # Iterate through the string
    for i in range(len(s)):
        # If the current char is a (
        if s[i] == "(":
            # Append it's index to the stack
            i_stack.append(i)
        # Else we pop the last element
        else:
            i_stack.pop()
            # if the stack is empty after the pop
            if len(i_stack) == 0:
                # Append the current index
                i_stack.append(i)
            else:
                # Else, calculate by subtracting 
                # the current index - the last index in the stack 
                if longest_sub < i - i_stack[-1]:
                    longest_sub = i - i_stack[-1]

    # Return the longest sub
    return longest_sub

if __name__ == "__main__":
    # Test string returns a 12
    # It works...
    test_string = ")(()()()()())"
    test_string_1 = "(()))())("
    test_string_2 = "()()"
    test_string_3 = "((()))"
    print(solution_prob_32(test_string))
    print(solution_prob_32(test_string_1))
    print(solution_prob_32(test_string_2))
    print(solution_prob_32(test_string_3))