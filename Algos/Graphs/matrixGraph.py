#!/usr/bin/python3


class Graph():
	def __init__(self, nodesStr):
		self.matrix = []
		self.nodesStr = nodesStr
		self.nodes = []
		self.nodeIdx = {}
		self.idxNode = {}
		self.numOfNodes = len(nodesStr)
		j = 0
		for i in nodesStr:
			self.nodeIdx[i] = j
			self.idxNode[j] = i
			self.nodes.append(i)
			j += 1

		for i in range(self.numOfNodes):
			self.matrix.append([0]* self.numOfNodes)
	

	def __str__(self):
		out = "s/d\t"
		for i in self.nodes:
			out += ("%s\t")%i
		out += "\n"
		
		j=0
		for i in self.nodes:
			out += "%s\t"% i
			for x in self.matrix[self.nodeIdx[i]]:
				out += "%d\t" % x
			out += "\n"
			j += 1

		return out
	
	def addBiEdge(self, source, destination, weight=1):
		self.matrix[self.nodeIdx[source]][self.nodeIdx[destination]] = weight
		self.matrix[self.nodeIdx[destination]][self.nodeIdx[source]] = weight
	
	def addUniEdge(self, source, destination, weight=1):
		self.matrix[self.nodeIdx[source]][self.nodeIdx[destination]] = weight
		
	
	def iterNeighbors(self, node):
		i = 0
		for neigh  in self.matrix[self.nodeIdx[node]]:
			if neigh > 0:
				yield self.idxNode[i]
			i += 1

	def iterNodes(self):
		for n in self.nodes:
			yield n


if __name__ == "__main__":
	g = Graph("0123")
	print(g)
	g.addUniEdge("2", "1")
	g.addUniEdge("0", "1")
	g.addUniEdge("1", "3")
	g.addUniEdge("0", "2")
	g.addUniEdge("0", "3")
	g.addUniEdge("2", "0")
	print(g)

	for n in g.iterNeighbors("0"):
		print(n)


