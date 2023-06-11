import lexicalParser
import syntacticParser

def main():
    path = 'D:/Codes/expressionParser/test/test.txt'
    Lparser = lexicalParser.lexicalParser()
    VtList = Lparser.parser(path=path)
    data = Lparser.getData()
    Sparser = syntacticParser.syntacticParser()
    Sparser.parser(VtList=VtList)

if __name__ == '__main__':
    main()