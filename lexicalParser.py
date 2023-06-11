def parser(path):
    expression = ''
    with open(path, 'r') as f:
        content = f.read()
        expression = content
        f.close()
    l = len(expression)
    tmp = ''
    for i in range(0, l):
        if expression[i] == ' ':
            continue
        elif i > 0 and not expression[i].isdigit():
            tmp = tmp + ' ' + expression[i]
        elif i > 0 and expression[i].isdigit() != expression[i - 1].isdigit():
            tmp = tmp + ' ' + expression[i]
        else:
            tmp = tmp + expression[i]
    VtList = tmp.split(' ')
    # print(list)
    with open('lexicalParser_out.txt', 'w') as w:
        for Vn in VtList:
            if Vn.isdigit():
                print(Vn, 'digit', file=w)
            elif Vn.isalpha():
                print(Vn, 'letter', file=w)
            elif Vn == '+':
                print(Vn, 'plus', file=w)
            elif Vn == '-':
                print(Vn, 'minus', file=w)
            elif Vn == '*':
                print(Vn, 'multiply', file=w)
            elif Vn == '/':
                print(Vn, 'divide', file=w)
            elif Vn == '^':
                print(Vn, 'power', file=w)
            elif Vn == '(':
                print(Vn, 'leftparen', file=w)
            elif Vn == ')':
                print(Vn, 'rightparen', file=w)
            elif Vn == '.':
                print(Vn, 'dot', file=w)
            else:
                print('Error')
                break
        w.close()
    return VtList