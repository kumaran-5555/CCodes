#!/usr/bin/python3
import os


class Node():
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None

		

class BinaryTree():
	
	def __init__(self, root):
		self.root = root


	#classmethod
	def _in_order(cls, node):
		if not node:
			return
		cls._in_order(node.left)
		print("%s "%node.val, end="")
		cls._in_order(node.right)

	def in_order(self):
		self._in_order(self.root)





if __name__ == "__main__":
	b = Node(1)
	b.left = Node(2)
	b.right = Node(3)
	b.left.left = Node(4)
	b.left.right = Node(5)
	b.right.left = Node(6)
	b.right.right = Node(7)

	tree = BinaryTree(b)
	tree.in_order()


		
	

