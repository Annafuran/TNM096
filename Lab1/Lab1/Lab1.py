import numpy as np
import random

#Calculating the herustic cost 
def heruCost(tempNode, nodeList):
    GoalNode = ["1", "2", "3", "4", "5", "6", "7", "8", "0"]
    heruMis = 0

    for i in range(9):
        if tempNode[i] != GoalNode[i]:
            heruMis = heruMis +1
    
    #Adding the herustic cost to the list of costs
    nodeList.append(heruMis)
    return nodeList

#Finding all the possible moves
def possibleMoves(NodeList):
    ZeroLocation = NodeList.index("0")
    tempNode=[]
    tempNode.extend(NodeList)
    CostList = []
    
    if NodeList.index("0")+3 <=8:
        temp = tempNode[NodeList.index("0")]
        tempNode[NodeList.index("0")] = tempNode[NodeList.index("0")+3]
        tempNode[NodeList.index("0")+3] = temp
        #Saving the heuristic cost in a list 
        CostList = heruCost(tempNode, CostList)
        tempNode=[]
        tempNode.extend(NodeList)
    else:
        CostList.append(1000)

    if NodeList.index("0")-3 >=0:
       temp = tempNode[NodeList.index("0")]
       tempNode[NodeList.index("0")] = tempNode[NodeList.index("0")-3]
       tempNode[NodeList.index("0")-3] = temp
       #Saving the heuristic cost in a list 
       CostList = heruCost(tempNode, CostList)
       tempNode=[]
       tempNode.extend(NodeList)
    else:
        CostList.append(1000)
    
    if NodeList.index("0")-1 >= 0:
       temp = tempNode[NodeList.index("0")]
       tempNode[NodeList.index("0")] = tempNode[NodeList.index("0")-1]
       tempNode[NodeList.index("0")-1] = temp
       #Saving the heuristic cost in a list 
       CostList = heruCost(tempNode, CostList)
       tempNode=[]
       tempNode.extend(NodeList)
    else:
        CostList.append(1000)
    
    if NodeList.index("0")+1 <= 8:
       temp = tempNode[NodeList.index("0")]
       tempNode[NodeList.index("0")] = tempNode[NodeList.index("0")+1]
       tempNode[NodeList.index("0")+1] = temp
       #Saving the heuristic cost in a list 
       CostList = heruCost(tempNode, CostList)
       tempNode=[]
       tempNode.extend(NodeList)
    else:
        CostList.append(1000)
    return CostList

def moveNode(StartNode, CostList):
    
    def swapPositions(list, pos1, pos2):
        list[pos1], list[pos2] = list[pos2], list[pos1]
        return list
    
    def switching(argument):
        switcher = {
        0: StartNode.index("0")+3,
        1: StartNode.index("0")-3,
        2: StartNode.index("0")-1,
        3: StartNode.index("0")+1          
        }
        return switcher.get(minIndex, "Invalid value")
    
    minIndex = CostList.index(min(CostList))
    switchLocation = switching(minIndex)
    ZeroLocation = StartNode.index("0")
   
    StartNode = swapPositions(StartNode, ZeroLocation, switchLocation)  

    print(StartNode)

    return StartNode


def puzzleGame(StartNode):
    counter = 0
    costList = []
    puzzelList = StartNode

    while True:
        if StartNode == None:
            print("No solution")
        else:
            costList = possibleMoves(puzzelList)
            puzzelList = moveNode(puzzelList, costList)

    return puzzelList


            #Kolla möjliga moves

            #Kolla vilken som är billigast

            #Välja next move


StartNode =  ["1", "2", "3", "4", "5", "6", "7", "8", "0"]
resultingGame = []

random.shuffle(StartNode)

resultingGame = puzzleGame(StartNode) 

print(resultingGame)
    