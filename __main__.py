import lexicalParser
import syntacticParser

def main():
    path = 'D:/Codes/expressionParser/test/test.txt'
    VtList = lexicalParser.parser(path=path)
    # print(VtList)
    
    syntacticParser.parser(VtList=VtList)

if __name__ == '__main__':
    main()