
import numpy as np
import random
import math
from heapq import heappush, heappop, nsmallest, heappushpop, heapreplace


#Calculating the herustic cost, multiple
def heruCost(tempNode):
    GoalNode = ["1", "2", "3", "4", "5", "6", "7", "8", "0"]
    heruMis = 0
    herDist = 0

    for i in range(9):
        if tempNode[i] != GoalNode[i]:
            heruMis = heruMis + 1   
    for i in tempNode:
        herDist += math.fabs(tempNode.index(i)- GoalNode.index(i))
    
    # f = h + g
    f = heruMis + herDist
    #Adding the herustic cost to the list of costs
    
    return f


#Finding all the possible moves
def possibleMoves(NodeList):
    ZeroLocation = NodeList.index("0")
    tempNode=[]
    tempNode.extend(NodeList)
    CostList = []
    ResultList = []
    result = {}
    
    if NodeList.index("0")+3 <=8:
        temp = tempNode[NodeList.index("0")]
        tempNode[NodeList.index("0")] = tempNode[NodeList.index("0")+3]
        tempNode[NodeList.index("0")+3] = temp
        #Saving the heuristic cost in a list 
        cost = heruCost(tempNode)
        ResultList.append([cost, tempNode, "down"])
        tempNode=[]
        tempNode.extend(NodeList)
    else:
        ResultList.append([1000, 1000, 1000])

    if NodeList.index("0")-3 >=0:
       temp = tempNode[NodeList.index("0")]
       tempNode[NodeList.index("0")] = tempNode[NodeList.index("0")-3]
       tempNode[NodeList.index("0")-3] = temp
       #Saving the heuristic cost in a list 
       cost = heruCost(tempNode)
       ResultList.append([cost, tempNode, "up"])
       tempNode=[]
       tempNode.extend(NodeList)
    else:
        ResultList.append([1000, 1000, 1000])
    
    if NodeList.index("0")-1 >= 0 and NodeList.index("0") != 3 and NodeList.index("0") != 6:
       temp = tempNode[NodeList.index("0")]
       tempNode[NodeList.index("0")] = tempNode[NodeList.index("0")-1]
       tempNode[NodeList.index("0")-1] = temp
       #Saving the heuristic cost in a list 
       cost = heruCost(tempNode)
       ResultList.append([cost, tempNode, "left"])  
       tempNode=[]
       tempNode.extend(NodeList)
    else:
        ResultList.append([1000, 1000, 1000])
    
    if NodeList.index("0")+1 <= 8 and NodeList.index("0") != 2 and NodeList.index("0") != 5:
       temp = tempNode[NodeList.index("0")]
       tempNode[NodeList.index("0")] = tempNode[NodeList.index("0")+1]
       tempNode[NodeList.index("0")+1] = temp
       #Saving the heuristic cost in a list 
       cost = heruCost(tempNode)
       ResultList.append([cost, tempNode, "right"])
       tempNode=[]
       tempNode.extend(NodeList)
    else:
        ResultList.append([1000, 1000, 1000])
    
    return ResultList

def puzzleGame(Initial_matrix, goal_matrix):

    #Hashtable
    closedList = {}
    #Heapqueue
    openList = []
    deepcounter = 0
    path = []
    generated_puzzle = []

    #push the initial_matrix with its heuristic cost to your open_list
    for item in possibleMoves(Initial_matrix):
        heappush(openList, item)
    
    while len(openList) != 0:
        #pop the matrix with the least cost from the open_list {we can call this matrix new_puzzle
                         
        new_puzzle = heappop(openList)
        #add to the path the direction chosen to generate this matrix {up, left, down,right}       

        path.append(new_puzzle[2])

        if new_puzzle[1] in closedList.values():
            continue
        if new_puzzle[1] == goal_matrix:
            return new_puzzle
        
        deepcounter += 1
        closedList[deepcounter] = new_puzzle[1]
        #MÅSTE TA MED DENNA I BERÄKNING TROR JAG?
        print(deepcounter)

        for generated_puzzle in possibleMoves(new_puzzle[1]):           
            #push to open_list(heuristic_cost_of_generated_puzzle,
            #generated_puzzle, direction_chosen_to_create_generated_puzzle)
            heappush(openList, generated_puzzle)
            
      
    return 0


ClosedList =  ["1", "8", "2", "0", "4", "3", "7", "6", "5"] 
GoalNode =  ["1", "2", "3", "4", "5", "6", "7", "8", "0"]
resultingGame = []

#random.shuffle(ClosedList)

resultingGame = puzzleGame(ClosedList, GoalNode) 

print(resultingGame)