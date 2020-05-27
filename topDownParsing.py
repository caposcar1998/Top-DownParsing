def createParsingTree(enterString, maxSizeTree, nonTerminalSymbols,startingSymbol, listProductions, counter = 0):
    
    
    res = [ele for ele in nonTerminalSymbols if(ele in enterString)]


    if (bool(res) and counter < int(maxSizeTree) ):

        for prod in  listProductions.get(res[0]):
            print("For everyProd")

            stringChanged = enterString.replace(res[0],prod,1 )
            print("Cambio string", stringChanged)
            counter +=1
        
            createParsingTree(stringChanged, maxSizeTree, nonTerminalSymbols,startingSymbol, listProductions, counter)
    else:
        print("Your final string is: ",enterString)