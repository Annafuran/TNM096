import numpy as np
import random

#GLOBAL VARIABLE


def changeGrandParent(newGrandParent):

    grandparent = newGrandParent

    return grandparent
   

#Calculating the herustic cost 
def heruCost(tempNode, nodeList, deepCounter):
    GoalNode = ["1", "2", "3", "4", "5", "6", "7", "8", "0"]
    heruMis = 0

    for i in range(9):
        if tempNode[i] != GoalNode[i]:
            heruMis = heruMis +1
    
    # f = h + g
    f = heruMis
    #Adding the herustic cost to the list of costs
    nodeList.append(f)
    return nodeList

#Finding all the possible moves
def possibleMoves(NodeList, deepCounter):
    ZeroLocation = NodeList.index("0")
    tempNode=[]
    tempNode.extend(NodeList)
    CostList = []
    
    if NodeList.index("0")+3 <=8:
        temp = tempNode[NodeList.index("0")]
        tempNode[NodeList.index("0")] = tempNode[NodeList.index("0")+3]
        tempNode[NodeList.index("0")+3] = temp
        #Saving the heuristic cost in a list 
        CostList = heruCost(tempNode, CostList, deepCounter)
        tempNode=[]
        tempNode.extend(NodeList)
    else:
        CostList.append(1000)

    if NodeList.index("0")-3 >=0:
       temp = tempNode[NodeList.index("0")]
       tempNode[NodeList.index("0")] = tempNode[NodeList.index("0")-3]
       tempNode[NodeList.index("0")-3] = temp
       #Saving the heuristic cost in a list 
       CostList = heruCost(tempNode, CostList, deepCounter)
       tempNode=[]
       tempNode.extend(NodeList)
    else:
        CostList.append(1000)
    
    if NodeList.index("0")-1 >= 0:
       temp = tempNode[NodeList.index("0")]
       tempNode[NodeList.index("0")] = tempNode[NodeList.index("0")-1]
       tempNode[NodeList.index("0")-1] = temp
       #Saving the heuristic cost in a list 
       CostList = heruCost(tempNode, CostList, deepCounter)
       tempNode=[]
       tempNode.extend(NodeList)
    else:
        CostList.append(1000)
    
    if NodeList.index("0")+1 <= 8:
       temp = tempNode[NodeList.index("0")]
       tempNode[NodeList.index("0")] = tempNode[NodeList.index("0")+1]
       tempNode[NodeList.index("0")+1] = temp
       #Saving the heuristic cost in a list 
       CostList = heruCost(tempNode, CostList, deepCounter)
       tempNode=[]
       tempNode.extend(NodeList)
    else:
        CostList.append(1000)
    return CostList

def moveNode(ClosedList, CostList, Visited, deepCounter, grandparent):

    OpenList = []
    
    def swapPositions(list, pos1, pos2):
        list[pos1], list[pos2] = list[pos2], list[pos1]
        resultinglist = list
        return resultinglist
    
    def switching(argument):
        switcher = {
        0: ClosedList.index("0")+3,
        1: ClosedList.index("0")-3,
        2: ClosedList.index("0")-1,
        3: ClosedList.index("0")+1          
        }
        return switcher.get(minIndex, "Invalid value")
    
    while True:
        minIndex = CostList.index(min(CostList))
        switchLocation = switching(minIndex)
        ZeroLocation = ClosedList.index("0")
        OpenList = swapPositions(ClosedList, ZeroLocation, switchLocation)
        print("hej")
        print(ZeroLocation)
        print(OpenList)
        print(ClosedList)
        if OpenList == grandparent:
            CostList[minIndex] = 1000;
        else:           
            grandparent = ClosedList
            ClosedList = OpenList;
            break
    
    return ClosedList, grandparent


def puzzleGame(ClosedList, GoalNode):
    counter = 0
    deepCounter = 0
    costList = []
    puzzelList = ClosedList
    visited = [12]
    grandparent = []

    while True:
        if ClosedList == None:
            print("No solution")
            break
        if  ClosedList == GoalNode:
            print("End of game")
            break
        else:
            costList = possibleMoves(puzzelList, deepCounter)
            puzzelList, grandparent = moveNode(puzzelList, costList, visited, deepCounter, grandparent)
            deepCounter += 1

    return puzzelList


ClosedList =  ["3", "1", "6", "8", "4", "5", "7", "2", "0"]
GoalNode =  ["1", "2", "3", "4", "5", "6", "7", "8", "0"]
resultingGame = []

#random.shuffle(ClosedList)

resultingGame = puzzleGame(ClosedList, GoalNode) 

print(resultingGame)
    