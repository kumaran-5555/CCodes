#!/usr/bin/python

import os
import collections
import sys
from node import Node

class BinaryTree():
	
	def __init__(self, root=None):
		self.root = root


	@classmethod
	def _in_order(cls, node):
		if not node:
			return
		cls._in_order(node.left)
		print("%s "%node.val, end="")
		cls._in_order(node.right)

	def in_order(self):
		print("InOrder:")
		self._in_order(self.root)
		print("")


	@classmethod
	def _pre_order(cls, node):
		if not node:
			return
		print("%s "%node.val, end="")
		cls._pre_order(node.left)
		cls._pre_order(node.right)

	def pre_order(self):
		print("PreOrder:")
		self._pre_order(self.root)
		print("")

		
	@classmethod
	def _post_order(cls, node):
		if not node:
			return
		cls._post_order(node.left)
		cls._post_order(node.right)
		print("%d "%node.val, end="")


	def post_order(self):
		print("PostOrder:")
		self._post_order(self.root)
		print("")


	def dfs(self):
		queue = collections.deque()
		print("DFS:")
		if not self.root:
			return
		
		queue.append(self.root)
		while len(queue):
			node = queue.pop()
			print("%d "%node.val, end="")
			if node.left:
				queue.append(node.left)
			if node.right:
				queue.append(node.right)
		
		print("")

	def bfs(self):
		queue = collections.deque()
		print("BFS")
		if not self.root:
			return
		queue.append(self.root)
		while len(queue):
			node = queue.popleft()
			print("%d "%node.val, end="")
			if node.left:
				queue.append(node.left)
			if node.right:
				queue.append(node.right)
		print("")

	def _build_from_inorder_preorder(cls, inorder, preorder, inS, inE, preS, preE):
		if inS >= inE or preS >= preE:
			return None
		node = Node(preorder[preS])
		
		for i in range(inS,inE):
			if inorder[i] == preorder[preS]:
				break
		sizeOfLeft = i-inS
		node.left = cls._build_from_inorder_preorder(inorder, preorder, inS, i, preS+1, preS+1+sizeOfLeft)
		node.right =  cls._build_from_inorder_preorder(inorder, preorder, i+1, inE, preS+1+sizeOfLeft, preE)
		return node

	def build_from_inorder_preorder(self, inorder, preorder):
		self.root = self._build_from_inorder_preorder(inorder, 
				preorder, 0, len(inorder), 0, len(preorder)) 



	def _build_from_inorder_postorder(cls, inorder, postorder, inS, inE, postS, postE):
		if inS >= inE or postS >= postE:
			return None
		node = Node(postorder[postE-1])
		for i in range(inS, inE):
			if inorder[i] == postorder[postE-1]:
				break
		sizeOfLeft = i-inS
		node.left = cls._build_from_inorder_postorder(inorder, postorder, inS, i, postS, postS+sizeOfLeft)
		node.right = cls._build_from_inorder_postorder(inorder, postorder, i+1, inE, postS+sizeOfLeft, postE-1)
		return node
		
	
	def build_from_inorder_postorder(self, inorder, postorder):
		self.root = self._build_from_inorder_postorder(inorder, 
				postorder, 0, len(inorder), 0, len(postorder))
	
	def print_top_view(self):
		topView = {}
		queue = collections.deque()
		queue.append((self.root, 0))

		while len(queue):
			(node, dist) = queue.popleft()
			if dist not in topView:
				topView[dist] = node.val
			if node.left:
				queue.append((node.left, dist-1))
			if node.right:
				queue.append((node.right, dist+1))
		print("TopView:")
		for i in sorted(topView.keys()):
			print("%d "%topView[i], end="")
		print("")


	def _print_left_view(cls, node, maxDistance, currDistance):
		if not node:
			return
		if currDistance > maxDistance[0]:
			print("%d "%node.val, end="")
			maxDistance[0] = currDistance
		cls._print_left_view(node.left, maxDistance, currDistance+1)			
		cls._print_left_view(node.right, maxDistance, currDistance+1)			

	def print_left_view(self):
		print("LeftView:")
		self._print_left_view(self.root, [-1], 0)
		print("")


	def _least_common_ancester(cls, node, state):
		
		canBeParent = False

		if not node:
			return
		if not state["n1Found"] and not state["n2Found"]:
			canBeParent = True
		if state["n1"] == node.val:
			state["n1Found"] = True
		elif state["n2"] == node.val:
			state["n2Found"] = True

		cls._least_common_ancester(node.left, state)
		cls._least_common_ancester(node.right, state)

		if state["n1Found"] and state["n2Found"] and canBeParent and not state["lca"]:
			state["lca"] = node
		return

	def least_common_ancester(self, n1, n2):
		state = {}
		state["n1Found"] = False
		state["n2Found"] = False
		state["n1"] = n1
		state["n2"] = n2
		state["lca"] = None
		self._least_common_ancester(self.root, state)
		if state["lca"]:
			print("Least Common Ancester %d"% state["lca"].val)
		else:
			print("No Least Common Ancester")


if __name__ == "__main__":
	b = Node(1)
	b.left = Node(2)
	b.right = Node(3)
	b.left.left = Node(4)
	b.left.right = Node(5)
	b.right.left = Node(6)
	b.right.right = Node(7)

	tree = BinaryTree()
	tree.build_from_inorder_preorder([4,2,5,1,6,3,7],[1,2,4,5,3,6,7])
	#tree.build_from_inorder_postorder([2,5,1,6,3,7],[5,2,6,7,3,1])


	tree.least_common_ancester(3, 2)


	sys.exit(1)
	tree.in_order()


	tree.pre_order()

		
	tree.post_order()
	

	tree.dfs()
	tree.bfs()

	tree.print_top_view()
	tree.print_left_view()


	b=Node(1)
	b.left = Node(2)
	b.right = Node(3)
	b.left.right = Node(4)
	b.left.right.right = Node(5)
	b.left.right.right.right= Node(6)

	tree = BinaryTree(b)
	tree.print_top_view()

	tree.print_left_view()

