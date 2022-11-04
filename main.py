import os
import codeParser


def main():
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
    main()
