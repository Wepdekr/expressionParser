import getLetter
import lexicalParser
import syntacticParser


def main():
    path = 'D:/Codes/expressionParser/test/test.txt'
    s = ''
    with open(path, 'r') as f:
        s = f.read()
        f.close()
    Lparser = lexicalParser.lexicalParser()
    tokens = Lparser.parser(expression=s)
    for i in tokens:
        if i.type == 'LETTER':
            x = input('%s = ' % i.value[0])
            getLetter.modify(i.value[0], int(x))

    print(tokens)
    # print(tokens[0].value, tokens[0].type)
    
    Sparser = syntacticParser.syntacticParser()
    result = Sparser.parse(expression=s)
    print(result)
    

if __name__ == '__main__':
    main()