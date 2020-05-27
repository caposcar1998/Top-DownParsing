from os import listdir
from os.path import isfile, join
from obtainInfoFile import openFile
from topDownParsing import createParsingTree
def main ():
    nonTerminalSymbols = None
    terminalSymbols = None
    startingSymbol = None
    listProductions = None
    print("Enter the string to check")
    enterString = input()
    print("Enter max depth of the tree")
    maxSizeTree = input()
    print("Select file from files, write full name with exttension and add files/, like ( files/test1.txt )")
    onlyfiles = [f for f in listdir("files") if isfile(join("files", f))]
    print(onlyfiles)
    fileSelected = input()

    nonTerminalSymbols = openFile(fileSelected)[0]
    terminalSymbols = openFile(fileSelected)[1]
    startingSymbol = openFile(fileSelected)[2]
    listProductions =openFile(fileSelected)[3]

    createParsingTree(enterString, maxSizeTree, nonTerminalSymbols, startingSymbol, listProductions)

if __name__ == "__main__":
    main()



