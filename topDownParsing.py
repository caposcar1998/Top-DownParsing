def createParsingTree(enterString, maxSizeTree, nonTerminalSymbols,startingSymbol, listProductions, counter = 0):
    
    
    res = [ele for ele in nonTerminalSymbols if(ele in enterString)]


    if counter == 0:
        res = "S"


    if (bool(res) and counter < int(maxSizeTree) ):
        for prod in  listProductions.get(res[0]):
            stringChanged = enterString.replace(res[0],prod,1 )
            counter +=1
            print(prod)
            createParsingTree(stringChanged, maxSizeTree, nonTerminalSymbols,startingSymbol, listProductions, counter)
    else:
        print("Your final string is: ",enterString)