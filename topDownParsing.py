def createParsingTree(enterString, maxSizeTree, nonTerminalSymbols,startingSymbol, listProductions, counter = 0):
    print()
    print("Productions",listProductions)
    print("Max Size tree",maxSizeTree)
    print("Starting symbol",startingSymbol)
    print()
    print('Looking for ' + enterString)

    res = [ele for ele in nonTerminalSymbols if(ele in startingSymbol)]
    print(res[0])
    for prod in listProductions.get(res[0]):
        counter = 0
        if (checkIfContinue(enterString, prod, nonTerminalSymbols)):
            print('|-' + prod)
            getNodesRec(enterString, prod, maxSizeTree, nonTerminalSymbols, listProductions, counter, False)   
        else:
            print('|-'+ prod + ' --> X')
    print()
    print('Tree height of ' + maxSizeTree)

def getNodesRec(enterString, prodString, maxSizeTree, nonTerminalSymbols, listProductions, counter, found):
    counter += 1
    if(enterString == prodString or counter >= int(maxSizeTree)):
        return
    else:
        res = [ele for ele in nonTerminalSymbols if(ele in prodString)]
        if(len(res) > 0):
            for prod in listProductions.get(res[0]):
                newString = prodString.replace(res[0], prod, 1)
                if (newString == enterString):
                    found = True
                    print(printLines(counter) + newString + " # Found! #")
                elif (checkIfContinue(enterString, newString, nonTerminalSymbols) and not found):
                    print(printLines(counter) + newString)
                    getNodesRec(enterString, newString, maxSizeTree, nonTerminalSymbols, listProductions, counter, found)
                else:
                    print(printLines(counter) + newString + ' --> X')


def printLines(counter):
    linesStr = '  |--'
    while(counter != 1):
        linesStr = '   ' + linesStr
        counter-=1
    return linesStr

def checkIfContinue(enterString, prodString, nonTerminalSymbols):
    count = 0
    if(len(enterString)==len(prodString)):
        while(count < len(enterString)):
            if((enterString[count]!=prodString[count]) and (prodString[count] not in nonTerminalSymbols)):
                return False
            count+=1
        return True

    elif(len(enterString)>len(prodString)):
        while(count < len(prodString)):
            if((enterString[count]!=prodString[count]) and (prodString[count] not in nonTerminalSymbols)):
                return False
            count+=1
        return True

    else:
        while(count < len(enterString)):
            if((enterString[count]!=prodString[count]) and (prodString[count] not in nonTerminalSymbols)):
                return False
            count+=1
        lastCount = 1 
        while(count < len(prodString)):
            if(prodString[count] not in nonTerminalSymbols):
                return False
            count+=1
        return True

    