# Solve the puzzle 8 in the breadth first search method. (Uninformed Search Strategies)
# in this project i use tree lib in python for implement state space.

from treelib import Node, Tree
import copy
from pprint import pprint
from functions import *

# enter your start state here:
startState=[3,1,2,4,7,5,6,0,8]
goalState=[0,1,2,3,4,5,6,7,8]
queue=[]    # bfs strategie use queue for tree scrolling
tree = Tree()   # create tree object.
tree.create_node(str(startState), str(startState))  # root node
queue.append(startState)    #append start state in queue

if(queue[0] == goalState):
    print("answer is start state...")
    exit(0)


while(1):
    # Create new states by moving white house
    childrenList=createChildren(queue[0])
    for item in childrenList:
        # Duplicate nodes are not added to the tree
        try:
            tree.create_node(str(item), str(item), str(queue[0]))       # expand tree
            queue.append(item)
        except:
            print("Duplicate error handled...")
        if item == goalState:
            finalAnswer = []
            print("**********\nThe answer was found\n**********")
            print("\nThe moves to get the answer:")

            currentNode = tree.get_node(str(item))
            finalAnswer.append(currentNode.tag)
            while(not tree.parent(str(currentNode.identifier)).is_root()):
                currentNode=tree.parent(str(currentNode.identifier))
                finalAnswer.append(currentNode.tag)
            finalAnswer.append(startState)
            pprint(finalAnswer)

            print("\n\ntree:")
            print(tree)
            exit(0)
    queue.remove(queue[0])
    print(tree)
    pprint(queue)
    print("_________________________________________________________________________")
    input()








































