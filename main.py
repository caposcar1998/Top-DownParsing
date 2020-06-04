#Tecnológico de Montettey
#Computational mathematics
#Proffesor Gilberto Huesca
#Students:
    #Oscar Contreras Palacios A01655772
    #Mauricio Acosta Hernández A01339392
#Tod down parsing tree 
#Part2 project

#If the string is found, the word "final" will appear after the string in the tree created

from os import listdir
from os.path import isfile, join
#Libraries used to read txt files
from obtainInfoFile import openFile
#Import to get information segmented from top down aprsing file
from topDownParsing import createParsingTree
#Import with algorithm of top down parsing

def main ():
    nonTerminalSymbols = None
    terminalSymbols = None
    startingSymbol = None
    listProductions = None
    #Variables that will take value of the tuple that file selected will return

    print("Enter the string to check")
    enterString = input()
    print("Enter max depth of the tree")
    maxSizeTree = input()
    #Inputs that the user will provide
    print("Select file from files")
    onlyfiles = [f for f in listdir("files") if isfile(join("files", f))]
    print(onlyfiles)
    fileSelected = input()
    #Select file from files inside files folder

    nonTerminalSymbols = openFile(fileSelected)[0]
    terminalSymbols = openFile(fileSelected)[1]
    startingSymbol = openFile(fileSelected)[2]
    listProductions =openFile(fileSelected)[3]
    #Assigning values from the tuple recieved from fileSelected

    createParsingTree(enterString, maxSizeTree, nonTerminalSymbols, startingSymbol, listProductions)
    #Function from topDownParsing that will execute the algorithm

if __name__ == "__main__":
    main()



