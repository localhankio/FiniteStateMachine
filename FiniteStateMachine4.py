import sys
import csv 
def main():

    argStr = sys.argv[1]
    alphabet = []
    finalStates = []
    finalLetters = []
    startState = ""
    startLetter = ""
    states = []
    transitionTable = []

    # read alphabet
    alph = open("./D4_Machine/alphabet.txt", 'r')
    for line in alph:
        line = line.rstrip('\n').replace('\\n','')
        alphabet.append(line)
    alph.close()

    #read final staes 
    finSt = open("./D4_Machine/finalStates.txt", 'r')
    for line in finSt:
        line = line.rstrip('\n').replace('\\n','')
        finalStates.append(line)
    finSt.close()

    #read startStates
    strSt = open("./D4_Machine/startState.txt", 'r')
    for line in strSt:
        line = line.rstrip('\n').replace('\\n', '\n')
        startState = line
    strSt.close()

    #read all states
    st = open("./D4_Machine/states.txt", 'r')
    for line in st:
        line = line.rstrip('\n').replace('\\n', '\n')
        states.append(line);
    st.close()

    #read transition table
    tranTbl = open("./D4_Machine/transitionTable.txt", 'r')
    for row in csv.reader(tranTbl, delimiter=',', quoting=csv.QUOTE_ALL):
        if (row):
            transitionTable.append(row)
        #print(row)
    tranTbl.close()
    if transitionTable[len(transitionTable)-1] == "\n":
        transitionTable.pop()

    currState = ""
    strIndex = 0
    isAccepted = True #whether or not word is accepted 
    print("Attempting to match string: ", argStr, "length = ",len(argStr))

    #get start letter from transition table, NOTE: DOES NOT WORK
    for row in transitionTable:
        if (startState == row[0] and row[2] != "NULL"):
            startLetter = row[1]
    startLetter = transitionTable[0][1]

    print("start letter is ", startLetter)

    for i in range (0, len(argStr)):
        if (argStr[i] == startLetter):
            #currState = "q0"
            if (checkWordValidity(argStr[i:], transitionTable, finalStates) == True):
                print("\n************************** \n Accepted ", argStr[i:], "\n**************************\n")
                continue 
            else: 
                print ("\n***Reject***\n")
                break
         
    print("Relevant FSA information:")
    print('\talphabet = ',alphabet)
    print('\tfinal state = ', finalStates)
    print('\tstart state = ', startState)
    print('\tstates = ', states)
    print('\ttransition table = ',transitionTable)
    print("done")

# @param currstate, the current state FSA is at
# param startst, start state
# @param substr, substring of strArgs
# @param tranTable, transitionTable only
# @param finState, finalState array
def checkWordValidity(substring, tranTable, finalArray):
    # print("\tin checkwordvalidity ", substring)
    # print(finalArray)
    currSt = "q0"
    #index = 0
    atFinalState = False
    #print("lenght of trnatable = ", len(tranTable))
    for index in range(0, len(substring)):
        if (atFinalState == False):
            for j in range(0, len(tranTable) +1):            
                #print("\t\tcurrst = ", currSt, "j = ", j, "index = ", index, ", ",substring[index])
                if (j < len(tranTable)):
                    if (currSt == tranTable[j][0] and substring[index] == tranTable[j][1]):
                        currSt = tranTable[j][2] 
                        #print("\t\tfound something, substr is ", substring[index], tranTable[j][1], " ", currSt, tranTable[j][2], " index= ", index)
                        # search if currstate == anhy final staltes
                        for k in range(0, len(finalArray)):
                            #print("\t\t\t currst", currSt ,"finArr[k]= ", finalArray[k])
                            if (currSt ==  finalArray[k]): #if currSTate is in final state and has extra strings 
                                #print("\t\t\tAT FINAL STATE")
                                atFinalState = True
                        if (currSt == "NULL"):
                            #print("got null", substring[index], j)
                            return False
                        break 
                else:
                    # print ("end of table ")
                    return False
        if (atFinalState and index == len(substring) -1 ):
            #print ("not final state anymore, index ", index, " letter = ", substring[index])
            return True
        if (atFinalState and index <= len(substring) - 2):
            atFinalState = False



if __name__ == "__main__": main()

#startstate always Q0?
#match start state on the transition table -