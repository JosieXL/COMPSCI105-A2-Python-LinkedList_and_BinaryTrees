#############################################
#	COMPSCI 105 S2 C, 2018              #
#	Assignment 2 Question 4             #
#                                           #
#	@author     Xiaolin Li and xli556   #
#	@version    17/10/2018              #
#############################################

from ListBinaryTree import ListBinaryTree

def buildTree(inorder,preorder):
    if not inorder:
        return None

    #first find the root value which is the first element of the preorder traversal
    root = preorder[0]
    root_inorder_index = inorder.find(root)

    #Then define the left_inorder, right_inorder, left_preorder and right_preorder
    #left/right are the left/right side of the tree
    #_inorder/_preorder is that using the value from inorder/preorder traversal
    left_inorder = inorder[:root_inorder_index]
    right_inorder = inorder[root_inorder_index+1:]
    left_preorder = preorder[1:root_inorder_index+1]
    right_preorder = preorder[root_inorder_index+1:]
        
    left_tree = buildTree(left_inorder, left_preorder)
    right_tree = buildTree(right_inorder, right_preorder)

    #build tree using ListBinaryTree class
    my_tree = ListBinaryTree(root, left_tree, right_tree)
    return my_tree

# YOUR IMPLEMENTATION

def postorder(tree):
    result = ""
    if tree != None:
        if tree.get_left_subtree() != None:
            result += postorder(tree.get_left_subtree())
        if tree.get_right_subtree() != None:
            result += postorder(tree.get_right_subtree())
        result += tree.get_value()
    return result
    #Need to be "return", or print the result it will print a "None" at the end of the string which is not what we want.
    

# YOUR IMPLEMENTATION


def main():
    print("Binary Tree construction:")
    inorder = input("Please enter the inorder sequence: ")
    preorder = input("Please enter the preorder sequence: ")
    tree =[]

    if (len(inorder) != len(preorder)):
        print("Error: Input strings have different length")
        exit(-1)

    tree = buildTree(inorder,preorder)

    print(tree)

    print("Postorder sequence of tree is:",postorder(tree))

main()

