


def openFile(fileName):
    nonTerminalSymbols = None
    terminalSymbols = None
    startingSymbol = None
    dictionaryProds =  {
        "S": [],
        }
    #Create variables in the start of the function so the could be used globally
    with open('files/' + fileName) as fp:
        line = fp.readline()
        cnt = 0
        while line:
            #Check line by line
            if(cnt == 0):
                nonTerminalSymbols = createTerminalSymbols(line)
                createDictionariesToFill(nonTerminalSymbols,dictionaryProds)
                #Check for nonTerminalSymbols and create a dictionary for every symbol
            if(cnt == 1):
                terminalSymbols = createNoTerminalSymbols(line)
                #Check for TerminalSymbols
            if(cnt == 2):
                startingSymbol = line
                #Check for startingSymbol
            if(cnt >= 3):
                createListProduction(nonTerminalSymbols, line, dictionaryProds)
                #From line 3 there are only pouctions, so we need to sort them by corresponding symbol
            line = fp.readline()
            cnt += 1
    fp.close()

    return nonTerminalSymbols, terminalSymbols, startingSymbol, dictionaryProds
    #Values returned to main function

def createDictionariesToFill(nonTerminalSymbols,dictionaryProds):
    for letter in nonTerminalSymbols:
        dictionaryProds[letter] = []
    #Create dictionary for every letter in nonTerminalSymbols


def createListProduction(nonTerminalSymbols,line, dictionaryProds):
    dictionaryProds[line[0]].append(line.split(">",1)[1].strip())
    #Here we get the information after the > sign, this information are the states
        

def createTerminalSymbols(line):
    nonTerminal = None
    newList = []
    nonTerminal = line.split(',')
    for element in nonTerminal:
        newList.append(element.strip())
    return newList
    #A list with the terminal symbols is created

def createNoTerminalSymbols(line):
    terminal = None
    newList = []
    nonTerminal = line.split(',')
    for element in nonTerminal:
        newList.append(element.strip())
    return newList
    #A list with the non terminal symbols is created