def parser(VtList):
    # print(VtList)
    stack = []
    revPolish = []
    for i in VtList:
        if i.isdigit() or i == '.' or i.isalpha():
            revPolish.append(i)
        elif i == '(':
            revPolish.append(')')
            stack.append('(')
        else:
            if i == ')':
                while len(stack) > 0 and stack[-1] != '(':
                    revPolish.append(stack[-1])
                    stack.pop()
                revPolish.append('(')
                stack.pop()
            elif i == '+' or i == '-':
                while len(stack) > 0 and stack[-1] != '(':
                    revPolish.append(stack[-1])
                    stack.pop()
                stack.append(i)
            elif i == '*' or i == '/':
                while len(stack) > 0 and (stack[-1] == '+' or stack[-1] == '-'):
                    revPolish.append(stack[-1])
                    stack.pop()
                stack.append(i)
            else:
                while len(stack) > 0 and stack[-1] != '^' and stack[-1] != '(':
                    revPolish.append(stack[-1])
                    stack.pop()
                stack.append(i)
    
    while len(stack) > 0:
        stack.pop()
    print(revPolish)