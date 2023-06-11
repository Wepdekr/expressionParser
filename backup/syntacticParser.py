import ply.yacc as yacc

from lexicalParser import tokens
from getLetter import map

def p_binary_operators(p):
    '''expression : expression PLUS term
                  | expression MINUS term
       term       : factor MULTIPLY term
                  | factor DIVIDE term
       factor     : base POWER factor'''
    # print(p[0], '=', p[1], p[2], p[3])
    if p[2] == '+':
        p[0] = p[1] + p[3]
    elif p[2] == '-':
        p[0] = p[1] - p[3]
    elif p[2] == '*':
        p[0] = p[1] * p[3]
    elif p[2] == '/':
        p[0] = p[1] / p[3]
    elif p[2] == '^':
        p[0] = p[1] ** p[3]

def p_pushdown(p):
    '''expression : term
       term       : factor
       factor     : base
       base       : identifier
                  | DIGIT
                  | real'''
    p[0] = p[1]

def p_base_expression(p):
    'base : LPAREN expression RPAREN'
    p[0] = p[2]

def p_indentifier(p):
    '''identifier : LETTER
                  | DIGIT LETTER'''
    # print(p[1], p[2])
    if len(p) == 2:
        p[0] = map[p[1]]
    else:
        p[0] = p[1] * map[p[2]]
    # print(p[0])

def p_real_digit(p):
    'real : DIGIT DOT DIGIT'
    real = str(p[1]) + '.' + str(p[3])
    p[0] = float(real)

def p_error(p):
    print('Syntax error')

parser = yacc.yacc()


class syntacticParser:
    def __init__(self) -> None:
        pass
    
    def parse(self, expression):
        ret = parser.parse(expression)
        return ret