


def openFile(fileName):
    nonTerminalSymbols = None
    terminalSymbols = None
    startingSymbol = None
    dictionaryProds =  {
        "S": [],
        }
    with open('files/' + fileName) as fp:
        line = fp.readline()
        cnt = 0
        while line:
            if(cnt == 0):
                nonTerminalSymbols = createTerminalSymbols(line)
                createDictionariesToFill(nonTerminalSymbols,dictionaryProds)
            if(cnt == 1):
                terminalSymbols = createNoTerminalSymbols(line)
            if(cnt == 2):
                startingSymbol = line
            if(cnt >= 3):
                createListProduction(nonTerminalSymbols, line, dictionaryProds)
            line = fp.readline()
            cnt += 1
    fp.close()

    return nonTerminalSymbols, terminalSymbols, startingSymbol, dictionaryProds

def createDictionariesToFill(nonTerminalSymbols,dictionaryProds):
    for letter in nonTerminalSymbols:
        dictionaryProds[letter] = []



def createListProduction(nonTerminalSymbols,line, dictionaryProds):
    dictionaryProds[line[0]].append(line.split(">",1)[1].strip())
    
        

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