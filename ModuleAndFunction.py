from treelib import Node, Tree
import copy
import heapq
from pprint import pprint


# In this function, the states resulting from the white house movement are obtained. Depending on where the white house is located.
def createChildren(givenState):
    resultList=[]
    emptySpaceLoc=givenState.index(0)
    if(emptySpaceLoc == 0):
        down = givenState[3]
        right = givenState[1]
        downState = copy.deepcopy(givenState)
        downState[3] = 0
        downState[0] = down
        resultList.append(downState)
        rightState = copy.deepcopy(givenState)
        rightState[1] = 0
        rightState[0] = right
        resultList.append(rightState )
        return resultList

    if(emptySpaceLoc == 1):
        down = givenState[4]
        left = givenState[0]
        right = givenState[2]
        downState = copy.deepcopy(givenState)
        downState[4] = 0
        downState[1] = down
        resultList.append(downState)
        rightState = copy.deepcopy(givenState)
        rightState[2] = 0
        rightState[1] = right
        resultList.append(rightState)
        leftState = copy.deepcopy(givenState)
        leftState[0] = 0
        leftState[1] = left
        resultList.append(leftState)
        return resultList

    if(emptySpaceLoc == 2):
        down = givenState[5]
        left = givenState[1]
        downState = copy.deepcopy(givenState)
        downState[5] = 0
        downState[2] = down
        resultList.append(downState)
        leftState = copy.deepcopy(givenState)
        leftState[1] = 0
        leftState[2] = left
        resultList.append(leftState)
        return resultList

    if(emptySpaceLoc == 3):
        top = givenState[0]
        down = givenState[6]
        right = givenState[4]
        topState = copy.deepcopy(givenState)
        topState[0] = 0
        topState[3] = top
        resultList.append(topState)
        rightState = copy.deepcopy(givenState)
        rightState[4] = 0
        rightState[3] = right
        resultList.append(rightState)
        downState = copy.deepcopy(givenState)
        downState[6] = 0
        downState[3] = down
        resultList.append(downState)
        return resultList

    if(emptySpaceLoc == 4):
        top=givenState[1]
        down=givenState[7]
        left=givenState[3]
        right=givenState[5]
        topState = copy.deepcopy(givenState)
        topState[1]=0
        topState[4]=top
        resultList.append(topState)
        downState = copy.deepcopy(givenState)
        downState[7] = 0
        downState[4] = down
        resultList.append(downState)
        rightState = copy.deepcopy(givenState)
        rightState[5] = 0
        rightState[4] = right
        resultList.append(rightState)
        leftState = copy.deepcopy(givenState)
        leftState[3] = 0
        leftState[4] = left
        resultList.append(leftState)
        return resultList

    if(emptySpaceLoc == 5):
        top = givenState[2]
        down = givenState[8]
        left = givenState[4]
        topState = copy.deepcopy(givenState)
        topState[2] = 0
        topState[5] = top
        resultList.append(topState)
        leftState = copy.deepcopy(givenState)
        leftState[4] = 0
        leftState[5] = left
        resultList.append(leftState )
        downState = copy.deepcopy(givenState)
        downState[8] = 0
        downState[5] = down
        resultList.append(downState)
        return resultList

    if(emptySpaceLoc == 6):
        top = givenState[3]
        right = givenState[7]
        topState = copy.deepcopy(givenState)
        topState[3] = 0
        topState[6] = top
        resultList.append(topState )
        rightState = copy.deepcopy(givenState)
        rightState[7] = 0
        rightState[6] = right
        resultList.append(rightState)
        return resultList

    if(emptySpaceLoc == 7):
        top = givenState[4]
        left = givenState[6]
        right = givenState[8]
        topState = copy.deepcopy(givenState)
        topState[4] = 0
        topState[7] = top
        resultList.append(topState)
        leftState = copy.deepcopy(givenState)
        leftState[6] = 0
        leftState[7] = left
        resultList.append(leftState)
        rightState = copy.deepcopy(givenState)
        rightState[8] = 0
        rightState[7] = right
        resultList.append(rightState )
        return resultList

    if(emptySpaceLoc == 8):
        top = givenState[5]
        left = givenState[7]
        topState = copy.deepcopy(givenState)
        topState[5] = 0
        topState[8] = top
        resultList.append(topState)
        leftState = copy.deepcopy(givenState)
        leftState[7] = 0
        leftState[8] = left
        resultList.append(leftState)
        return resultList


# H2(): Manhattan Distance Of Tiles Out Of Place. (heuristic function for A*)
def H2(givenState):
    positionForTiles=[[0,0],[0,1],[0,2],[1,0],[1,1],[1,2],[2,0],[2,1],[2,2]]        # position for tiles in goal state. (in two dimensional list for puzzle)
    hValue=0
    for i in range(0,len(givenState)):
        # print(positionForTiles[i])
        # print(positionForTiles[givenState[i]])
        # print( (max(positionForTiles[i][0],positionForTiles[givenState[i]][0]) - min(positionForTiles[i][0],positionForTiles[givenState[i]][0])) +
        #        (max(positionForTiles[i][1], positionForTiles[givenState[i]][1]) - min(positionForTiles[i][1], positionForTiles[givenState[i]][1])) )
        hValue += (max(positionForTiles[i][0],positionForTiles[givenState[i]][0]) - min(positionForTiles[i][0],positionForTiles[givenState[i]][0])) + \
                  (max(positionForTiles[i][1], positionForTiles[givenState[i]][1]) - min(positionForTiles[i][1], positionForTiles[givenState[i]][1]))
    #     print("___________")
    # print("h=" , hValue)
    return hValue

# implementation for priority queue
# I use heapq module in python for priority queue.
class priority_queue:
    # Initialize the instance
    def __init__(self):
        # Create a list to use as the queue
        self._queue = []
        # Create an index to use as ordering
        self._index = 0

    # Create a function to add a task to the queue
    def add_task(self, item, priority):
        # Push the arguments to the _queue using a heap
        heapq.heappush(self._queue, (priority, self._index, item))
        # Add one to the index
        self._index += 1

    # Create a function to get the next item from the queue
    def next_task(self):
        # Return the next item in the queue
        return heapq.heappop(self._queue)[-1]

    def show(self):
        pprint(self._queue)


# This class is used in A* strategy for saving information about each node.
class nodeInfo(object):
        def __init__(self, state , h , g ):
            self.state = state
            self.h = h
            self.g = g
            self.f = h+g
            self.info = [self.state,self.f]


















