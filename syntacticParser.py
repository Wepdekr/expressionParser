import ply.yacc as yacc
from lexicalParser import tokens
from modifyLetterVal import letters

class Node:
    def __init__(self, type, value, children=None):
        self.type = type
        self.value = value
        if children:
            self.children = children
        else:
            self.children = [ ]

def p_binary_operators(p):
    '''expression : expression PLUS term
                  | expression MINUS term
       term       : factor MULTIPLY term
                  | factor DIVIDE term
       factor     : base POWER factor'''
    # print(p[0], '=', p[1], p[2], p[3])
    if p[2] == '+':
        p[0] = Node('expression', p[1].value + p[3].value, [p[1], Node('PLUS', '+'), p[3]])
        # p[0] = p[1] + p[3]
    elif p[2] == '-':
        p[0] = Node('expression', p[1].value - p[3].value, [p[1], Node('MINUS', '-'), p[3]])
        # p[0] = p[1] - p[3]
    elif p[2] == '*':
        p[0] = Node('term', p[1].value * p[3].value, [p[1], Node('MULTIPLY', '*'), p[3]])
        # p[0] = p[1] * p[3]
    elif p[2] == '/':
        p[0] = Node('term', p[1].value / p[3].value, [p[1], Node('DIVIDE', '/'), p[3]])
        # p[0] = p[1] / p[3]
    elif p[2] == '^':
        p[0] = Node('factor', p[1].value ** p[3].value, [p[1], Node('POWER', '^'), p[3]])
        # p[0] = p[1] ** p[3]

# def p_pushdown(p):
#     '''expression : term
#        term       : factor
#        factor     : base
#        base       : identifier
#                   | DIGIT
#                   | real'''
#     p[0] = p[1]

def p_expression_term(p):
    'expression : term'
    p[0] = Node('expression', p[1].value, [p[1]])

def p_term_factor(p):
    'term : factor'
    p[0] = Node('term', p[1].value, [p[1]])

def p_factor_base(p):
    'factor : base'
    p[0] = Node('factor', p[1].value, [p[1]])

def p_base_identifier(p):
    'base : identifier'
    p[0] = Node('base', p[1].value, [p[1]])

def p_base_DIGIT(p):
    'base : DIGIT'
    p[0] = Node('base', p[1], [Node('DIGIT', p[1])])

def p_base_real(p):
    'base : real'
    p[0] = Node('base', p[1].value, [p[1]])

def p_base_expression(p):
    'base : LPAREN expression RPAREN'
    p[0] = Node('base', p[2].value, [Node('LPAREN', '('), p[2], Node('RPAREN', ')')])

def p_indentifier(p):
    '''identifier : LETTER
                  | DIGIT LETTER'''
    # print(p[1], p[2])
    if len(p) == 2:
        p[0] = Node('identifier', letters.getMap(p[1]), [Node('LETTER', p[1])])
        # p[0] = letters.getMap(p[1])
    else:
        p[0] = Node('identifier', p[1] * letters.getMap(p[2]), [Node('DIGIT', p[1]), Node('LETTER', letters.getMap(p[2]))])
        # p[0] = p[1] * letters.getMap(p[2])
    # print(p[0])

def p_real_digit(p):
    'real : DIGIT DOT DIGIT'
    real = str(p[1]) + '.' + str(p[3])
    p[0] = Node('real', float(real), [Node('DIGIT', p[1]), Node('Dot', '.'), Node('DIGIT', p[3])])
    # p[0] = float(real)

def p_error(p):
    print('Syntax error')

parser = yacc.yacc()

def search(node, dep):
    tabs = ''
    if dep > 0:
        tabs = dep * '  '
    print(tabs, node.type, node.value)
    if node.children:
        for i in node.children:
            search(i, dep + 1)


class syntacticParser:
    def __init__(self) -> None:
        pass
    
    def parse(self, expression):
        ret = parser.parse(expression)
        return ret
    
    def getValue(self, expression):
        root = self.parse(expression=expression)
        return root.value