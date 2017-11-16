# Solve the puzzle 8 in the depth first search method. (Uninformed Search Strategies)
# in this project i use tree lib in python for implement state space.

from treelib import Node, Tree
import copy
from pprint import pprint
from ModuleAndFunction import *

# enter your start state here:
startState=[7,2,4,5,0,6,8,3,1]
#[3,1,2,4,7,5,6,0,8]
#[3,1,2,4,7,5,6,0,8]
# enter your goal state here.
goalState=[0,1,2,3,4,5,6,7,8]
stack=[]     # dfs strategie use stack for tree scrolling
tree = Tree()  # create tree object.

tree.create_node( str(startState) , str(startState) , data=startState)  # root node
stack.append(tree.get_node(str(startState)))        #append start state in stack

while(1):
    currentParent = stack.pop()
    # check for goal state
    if currentParent.data == goalState:
        print("**********\nThe answer was found\n**********")
        print("\nStack:")
        pprint(stack)
        print("\n\nTree:\n",tree)
        exit(0)

    # Create new states by moving white house
    childrenList=createChildren(currentParent.data)
    for item in childrenList:
        # Duplicate nodes are not added to the tree
        try:
            nodeObj = tree.create_node(str(item), str(item), parent=currentParent.tag, data=item)
            stack.append(nodeObj)
        except:
            print("Duplicate error handled...")
    pprint(stack)
    print(tree)
    print("___________________________________________________________________________")
    input()










































