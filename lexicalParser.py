class lexicalParser:
    def __init__(self):
        self.__data = []
    
    def parser(self, path):
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
        for Vn in VtList:
            if Vn.isdigit():
                self.__data.append((Vn, 'digit'))
            elif Vn.isalpha():
                self.__data.append((Vn, 'letter'))
            elif Vn == '+':
                self.__data.append((Vn, 'plus'))
            elif Vn == '-':
                self.__data.append((Vn, 'minus'))
            elif Vn == '*':
                self.__data.append((Vn, 'multiply'))
            elif Vn == '/':
                self.__data.append((Vn, 'divide'))
            elif Vn == '^':
                self.__data.append((Vn, 'power'))
            elif Vn == '(':
                self.__data.append((Vn, 'leftparen'))
            elif Vn == ')':
                self.__data.append((Vn, 'rightparen'))
            elif Vn == '.':
                self.__data.append((Vn, 'dot'))
            else:
                print('Error')
                break

        return VtList
    
    def getData(self):
        return self.__data