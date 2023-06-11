class syntacticParser:
    def __init__(self):
        self.T = []
        self.root = self.node()

    class node:
        def __init__(self):
            self.son = []
            self.val = ''
            self.type = ''
        
        def __init__(self, val, type):
            self.son = []
            self.val = val
            self.type = type
        
        def getVal(self):
            return self.val
        
        def addSon(self, s):
            self.son.append(s)

    def getRevPolish(self, VtList):
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

    def getReal(intSec, decSec):
        real = str(intSec) + '.' + str(decSec)
        return float(real)

    def buildTree(self, revPolish):
        stackE = []
        stackT = []
        for i in revPolish:
            if i.isdigit() and stackE[-1] == '.':
                dot = stackT.pop()
                intSec = stackT.pop()
                decSec = self.node(val=int(i), type='digit')
                real = self.getReal(intSec=intSec.getVal(), decSec=decSec.getVal())
                n = self.node(val=real, type='real')
                n.addSon(intSec)
                n.addSon(dot)
                n.addSon(decSec)
                stackT.append(n)
                stackE.pop()
                stackE.pop()
                stackE.append(real)
            elif i.isdigit():
                stackE.append(i)
                stackT.append(self.node(val=int(i), type='digit'))
            elif i == ')':
                stackE.append(i)
                stackT.append(self.node(val=i, type='rightparen'))
            elif i == '+':
                pass

    def parser(self, VtList):
        revPolish = self.getRevPolish(VtList=VtList)
        # print(revPolish)
        self.buildTree(revPolish=revPolish)