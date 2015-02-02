#!/usr/bin/python3

# http://www.geeksforgeeks.org/topological-sorting/

import collections
from matrixGraph import Graph



def dfs(graph):
	visited = {}
	for n in  graph.iterNodes():
		visited[n] = False
	
	for n in visited:
		if not visited[n]:
			_dfs(graph, n, visited)

def _dfs(graph, start, visited):
	stack = collections.deque()
	stack.append(start)

	print("DFS: ",end="")
	while len(stack):
		node = stack.pop()
		print(node, end="")
		for neigh in graph.iterNeighbors(node):
			if not visited[neigh]:
				stack.append(neigh)
	
		visited[node] = True
	
	print("")
	

def dfsRecursive(graph, start, visited):
	if start in visited:
		return
	print(start, end="")
	visited[start] = True
	for neigh in graph.iterNeighbors(start):
		dfsRecursive(graph, neigh, visited)



def bfs(graph, start):
	queue = collections.deque()
	queue.append(start)
	visited = {}
	
	print("BFS: ",end="")

	while(len(queue)):
		node = queue.popleft()
		print(node, end="")
		for neigh in graph.iterNeighbors(node):
			if neigh not in visited:
				queue.append(neigh)
		visited[node] = True
	print("")


def _cycleDetectiion(graph, start, visited):
	stack = collections.deque()
	stack.push(start)
	while (len(stack)):
		node = stack.pop()
		for neigh in graph.iterNeighbors(node):
			if visited[neigh]:
				return True
			stack.append(neigh)
		visited[node] = True
	return False


def cycleDetection(graph):
	visited = {}
	for n in graph.iterNodes():
		visited[n] = False
	
	for n in visited:
		if not visited[n]:
			if _cycleDetection(graph, n, visited):
				return True
	
	return False


	
def _toplogicalSort(graph, start, state):
	

def topologicalSort(graph):
	if cycleDetection(graph):
		print("Graph is DAG, contains cycle")
		return
	


if __name__ == "__main__":
	g = Graph("0123")
	g.addBiEdge("0","2")
	g.addUniEdge("0","1")
	g.addUniEdge("1","2")
	g.addUniEdge("2","3")
	print(g)
	dfs(g)
	print(g)
	#dfsRecursive(g, "2", {})
	bfs(g, "2")


	g = Graph("012345")
	g.addUniEdge("5","2")
	g.addUniEdge("5","0")
	g.addUniEdge("4","0")
	g.addUniEdge("4","1")
	g.addUniEdge("2","3")
	g.addUniEdge("3","1")

	dfs(g)


