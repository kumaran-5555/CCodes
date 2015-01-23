#!/usr/bin/python

__doc__ = "4.9 fifth edition"

from node import Node


def print_path(pathList, node, sumK):
	if not node:
		return
	pathList.append(node.val)
	currSum = 0
	for i in range(len(pathList)-1, -1, -1):
		currSum += pathList[i]
		if currSum == sumK:
			print(pathList[i:])
		
	print_path(pathList, node.left, sumK)
	print_path(pathList, node.right, sumK)
	pathList.pop()



if __name__ == "__main__":
	root = Node(1)
	root.left = Node(2)
	root.right = Node(4)
	root.left.left =  Node(2)
	root.left.left.right = Node(3)
	root.left.left.right.left = Node(-3)
	root.right.left = Node(-2)
	root.right.left.right = Node(3)
	root.right.right = Node(-4)
	root.right.right.right = Node(6)
	root.right.right.right.left = Node(-2)

	pathList = []
	print_path(pathList, root, 5)

