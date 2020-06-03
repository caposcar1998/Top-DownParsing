def createParsingTree(enterString, maxSizeTree, nonTerminalSymbols,startingSymbol, listProductions, counter = 0):
    
    print(listProductions)
    print(maxSizeTree)
    print(nonTerminalSymbols)
    print(startingSymbol)

    res = [ele for ele in nonTerminalSymbols if(ele in startingSymbol)]
    print(res[0])
    for prod in listProductions.get(res[0]):
        counter = 0
        getNodesRec(enterString, prod, maxSizeTree, nonTerminalSymbols, listProductions, counter)

def getNodesRec(enterString, prodString, maxSizeTree, nonTerminalSymbols, listProductions, counter):
    counter += 1
    print(counter)
    if(enterString == prodString or counter >= int(maxSizeTree)):
        if(enterString == prodString):
            print('Valor Final ' + prodString)
        else:
            print('Altura Maxima encontrada. ' + prodString)
        return
    else:
        res = [ele for ele in nonTerminalSymbols if(ele in prodString)]
        print(listProductions.get(res[0]))
        for prod in listProductions.get(res[0]):
            newString = prodString.replace(res[0], prod, 1)
            print(newString)
            getNodesRec(enterString, newString, maxSizeTree, nonTerminalSymbols, listProductions, counter)


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