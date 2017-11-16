# Solve the puzzle 8 in the A* method. (informed Search Strategies)
# in this project i use tree lib in python for implement state space.
# and heapq lib for implement priority queue.
# https://chrisalbon.com/python/priority_queues.html

from treelib import Node, Tree
import copy
from pprint import pprint
from ModuleAndFunction import *


# enter your start state here:
startState=[7,2,4,5,0,6,8,3,1]
#[3,1,2,4,7,5,6,0,8]
# enter your goal state here.
goalState=[0,1,2,3,4,5,6,7,8]
priorityQueue=priority_queue()     # A* strategie use priority queue for tree scrolling
tree = Tree()  # create tree object.

h2ForRoot=H2(startState)
rootInfo=nodeInfo(startState,h2ForRoot,0)
#print(rootInfo.state , rootInfo.g , rootInfo.h , rootInfo.info)
tree.create_node( str(startState) , str(startState) , data=rootInfo)  # root node
priorityQueue.add_task(tree.get_node(str(startState)) , h2ForRoot+0 )     # add start state in priority queue

# print(tree.get_node(str(startState)).data.info)
# tree.show(data_property="info")

if startState == goalState:
    print("**********\nThe answer was found\n**********")
    exit(0)

while(1):
    currentParent=priorityQueue.next_task()
    # Create new states by moving white house
    childrenList = createChildren(currentParent.data.state)
    # calculate g parameter for children
    childrenG = currentParent.data.g + 1
    for item in childrenList:
        # calculate h parameter for children
        childrenH = H2(item)
        # Duplicate nodes are not added to the tree
        try:
            # adding children to tree
            nodeObj = tree.create_node(str(item), str(item), parent=currentParent.identifier, data=nodeInfo(item,childrenH,childrenG))
            # addning tree node to priority queue
            priorityQueue.add_task( nodeObj , childrenH + childrenG )
        except:
            print("Duplicate error handled...")

        # check for goal state.
        if item == goalState:
            print("**********\nThe answer was found\n**********\n\ntree:")
            tree.show(data_property="info")
            exit(0)

    tree.show(data_property="info")
    print("___________________________________________________________________________")
    #input()































