import os
import codeParser


def main():

    # path = "C:\\Users\\dimon\\Desktop\\labBuffer\\src\\main\\java\\banks\\account\\Account.java".split('\\')[:-1]
    # fileName = "C:\\Users\\dimon\\Desktop\\labBuffer\\src\\main\\java\\banks\\account\\Account.java".split('\\')[-1]
    # print("\\".join(path))
    # print(fileName)
    # try:
    #     os.makedirs("C:\\Users\\dimon\\Desktop\\labBuffer\\src\\main\\java\\banks\\entity")
    # except:
    #     file = open("C:\\Users\\dimon\\Desktop\\labBuffer\\src\\main\\java\\banks\\account\\Account.java", 'w+')
    #     file.write("123")
    # os.makedirs("C:\\Users\\dimon\\Desktop\\labBuffer\\src\\main\\java\\banks\\entity")
    # testFile = open("C:\\Users\\dimon\\Desktop\\labBuffer\\src\\main\\java\\banks\\account\\Account.java", "w+")
    # testFile.write("123")
    docPath = "C:\\Users\\dimon\\Desktop\\techReports\\Отчет1ЛабораторнаяПреженцовДмитрийИгоревичМ32051.docx"
    codeFiles = codeParser.parse(docPath)

    for codeFile in codeFiles:
        try:
            print(codeFile.dirPath)
            os.makedirs(codeFile.dirPath)
        finally:
            print(codeFile.filePath)
            with open(codeFile.filePath, 'w+') as file:
                for code in codeFile.code:
                    file.write(code)




if __name__ == '__main__':
    # print(os.path.join("C:/Users/dimon/Desktop/labBuffer", "labBuffer/src/main/java/banks/account"))
    # os.makedirs(os.path.join("C:/Users/dimon/Desktop/labBuffer", "src/main/java/banks/account"))
    main()