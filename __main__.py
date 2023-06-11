import lexicalParser
import syntacticParser

def main():
    path = 'D:/Codes/expressionParser/test/test.txt'
    Lparser = lexicalParser.lexicalParser()
    VtList = Lparser.parser(path=path)
    data = Lparser.getData()
    syntacticParser.parser(VtList=VtList)

if __name__ == '__main__':
    main()