def createParsingTree(enterString, maxSizeTree, nonTerminalSymbols,startingSymbol, listProductions, counter = 0):
    
    
    res = [ele for ele in nonTerminalSymbols if(ele in enterString)]

    

    if (bool(res) ):
        print("String entrada ",enterString)
        print("Datoa modificar", res[0])
        print("Producciones para res: ", listProductions.get(res[0]))
        #Segundo arreglo cambiar por valor que se parezca al sttring orignila
        print("Valor que se va a cambiar", listProductions.get(res[0])[1])
        stringChanged = enterString.replace(res[0],listProductions.get(res[0])[1],1 )
        print("Cambio string", stringChanged)
        counter +=1
        
        createParsingTree(stringChanged, maxSizeTree, nonTerminalSymbols,startingSymbol, listProductions, counter)
    else:
        print("Your final string is: ",enterString)