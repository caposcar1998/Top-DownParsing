def createParsingTree(enterString, maxSizeTree, nonTerminalSymbols,startingSymbol, listProductions, counter = 0):
    
    print("Productions",listProductions)
    print("Max Size tree",maxSizeTree)
    print("Starting symbol",startingSymbol)

    res = [ele for ele in nonTerminalSymbols if(ele in startingSymbol)]
    print(res[0])
    for prod in listProductions.get(res[0]):
        counter = 0
        print(prod)
        getNodesRec(enterString, prod, maxSizeTree, nonTerminalSymbols, listProductions, counter)

def getNodesRec(enterString, prodString, maxSizeTree, nonTerminalSymbols, listProductions, counter):
    counter += 1
    if(enterString == prodString or counter >= int(maxSizeTree)):
        return
    else:
        res = [ele for ele in nonTerminalSymbols if(ele in prodString)]
        for prod in listProductions.get(res[0]):
            try:
                newString = prodString.replace(res[0], prod, 1)
                if (newString == enterString):
                    print(printLines(counter) + newString+ " final")
                else:
                    print(printLines(counter) + newString)
                getNodesRec(enterString, newString, maxSizeTree, nonTerminalSymbols, listProductions, counter)
            except:
                print("End")


def printLines(counter):
    linesStr = '--'
    while(counter != 1):
        linesStr += '--'
        counter-=1
    return linesStr
