import lexicalParser
# import syntacticParser

def main():
    path = 'D:/Codes/expressionParser/test/test.txt'
    tmp = lexicalParser.lexicalParser()
    VtList = tmp.parser(path=path)
    data = tmp.getData()
    print(data)
    # print(VtList)
    
    # syntacticParser.parser(VtList=VtList)

if __name__ == '__main__':
    main()