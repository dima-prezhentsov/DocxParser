class CodeFile:
    def __init__(self, dirPath, filePath):
        self.dirPath = dirPath
        self.filePath = filePath
        self.code = []

    def addCodeRow(self, row):
        self.code.append(row)