


def openFile(fileName):
    nonTerminalSymbols = None
    terminalSymbols = None
    startingSymbol = None
    listProductions = None
    with open("files/test1.txt") as fp:
        line = fp.readline()
        cnt = 0
        while line:
            if(cnt == 0):
                nonTerminalSymbols = createTerminalSymbols(line)
                listProductions = createDictionariesToFill(nonTerminalSymbols)
            if(cnt == 1):
                terminalSymbols = createNoTerminalSymbols(line)
            if(cnt == 2):
                startingSymbol = line
            if(cnt >= 3):
                createListProduction(nonTerminalSymbols, line, listProductions)
            line = fp.readline()
            cnt += 1
    fp.close()

    return nonTerminalSymbols, terminalSymbols, startingSymbol, listProductions

def createDictionariesToFill(nonTerminalSymbols):
    listOfProductions = []
    for letter in nonTerminalSymbols:
        prod = {
        "name": letter,
        "prodStates": []
        }
        listOfProductions.append(prod)
    return listOfProductions

def createListProduction(nonTerminalSymbols,line, listProductions):
    for letter in listProductions:
        if(letter.get("name") == line[0]): 
            letter["prodStates"].append(line.split(">",1)[1].strip())
        
        

def createTerminalSymbols(line):
    nonTerminal = None
    newList = []
    nonTerminal = line.split(',')
    for element in nonTerminal:
        newList.append(element.strip())
    return newList

def createNoTerminalSymbols(line):
    terminal = None
    newList = []
    nonTerminal = line.split(',')
    for element in nonTerminal:
        newList.append(element.strip())
    return newList