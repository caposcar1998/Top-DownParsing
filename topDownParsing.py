def createParsingTree(enterString, maxSizeTree, nonTerminalSymbols,startingSymbol, listProductions, counter = 0):
    
    print(listProductions)
    print(maxSizeTree)
    print(nonTerminalSymbols)
    print(startingSymbol)

    res = [ele for ele in nonTerminalSymbols if(ele in startingSymbol)]
    print(res[0])
    for prod in listProductions.get(res[0]):
        counter = 0
        print(prod)
        getNodesRec(enterString, prod, maxSizeTree, nonTerminalSymbols, listProductions, counter)

def getNodesRec(enterString, prodString, maxSizeTree, nonTerminalSymbols, listProductions, counter):
    counter += 1
    if(enterString == prodString or counter >= int(maxSizeTree)):
        #if(enterString == prodString):
            #print('Valor Final ' + prodString)
        #else:
            #print('Altura Maxima encontrada. ' + prodString)
        return
    else:
        res = [ele for ele in nonTerminalSymbols if(ele in prodString)]
        for prod in listProductions.get(res[0]):
            newString = prodString.replace(res[0], prod, 1)
            print(printLines(counter) + newString)
            getNodesRec(enterString, newString, maxSizeTree, nonTerminalSymbols, listProductions, counter)


def printLines(counter):
    linesStr = '--'
    while(counter != 1):
        linesStr += '--'
        counter-=1
    return linesStr

    #if counter == 0:
    #    res = "S"


    #if (bool(res) and counter < int(maxSizeTree) ):
    #    for prod in  listProductions.get(res[0]):
    #        stringChanged = enterString.replace(res[0],prod,1 )
    #        #print(enterString.replace(res[0],prod,1))
    #        counter +=1
    #        print(prod)
    #        print(stringChanged)
    #        createParsingTree(stringChanged, maxSizeTree, nonTerminalSymbols,startingSymbol, listProductions, counter)
    #else:
    #    print("Your final string is: ",enterString)