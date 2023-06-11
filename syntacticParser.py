def getRevPolish(VtList):
    stack = []
    ret = []
    for i in VtList:
        if i.isdigit() or i == '.' or i.isalpha():
            ret.append(i)
        elif i == '(':
            ret.append(')')
            stack.append('(')
        else:
            if i == ')':
                while len(stack) > 0 and stack[-1] != '(':
                    ret.append(stack[-1])
                    stack.pop()
                ret.append('(')
                stack.pop()
            elif i == '+' or i == '-':
                while len(stack) > 0 and stack[-1] != '(':
                    ret.append(stack[-1])
                    stack.pop()
                stack.append(i)
            elif i == '*' or i == '/':
                while len(stack) > 0 and (stack[-1] == '+' or stack[-1] == '-'):
                    ret.append(stack[-1])
                    stack.pop()
                stack.append(i)
            else:
                while len(stack) > 0 and stack[-1] != '^' and stack[-1] != '(':
                    ret.append(stack[-1])
                    stack.pop()
                stack.append(i)
    
    while len(stack) > 0:
        ret.append(stack[-1])
        stack.pop()
    
    return ret

def parser(VtList):
    revPolish = getRevPolish(VtList=VtList)
    print(revPolish)
    