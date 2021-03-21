def reverseInParentheses(s):
    stack = []
    for i in s:
        if i == ")":
            t = ""
            while stack[-1] != "(":
                t += stack.pop()
            stack.pop()
            for j in t:
                stack.append(j)
        else:
            stack.append(i)

    return "".join(stack)
