#!/usr/bin/python3
__author__ = 'kumaran'

#!/usr/bin/python3
__author__ = 'kumaran'


import heapq
import sys

class Graph():
    def __init__(self, adjacencyMatrix):
        self.adjacencyMatrix = adjacencyMatrix
        self.size = len(self.adjacencyMatrix)


    def __str__(self):
        for i in range(self.size):
            print(self.adjacencyMatrix[i])
        return ""


class Solution():
    def bellmanFordShortestPath(self, graph, sourceIdx):
        predcesor = {}
        distance = [float("inf")] * graph.size
        distance[sourceIdx] = 0
        predcesor[sourceIdx] = None


        for k in range(graph.size-1):
            for i in range(graph.size):
                for j in range(graph.size):
                    if graph.adjacencyMatrix[i][j]:
                        if distance[j] > distance[i] + graph.adjacencyMatrix[i][j]:
                            distance[j] = distance[i] + graph.adjacencyMatrix[i][j]
                            predcesor[j] = i

        for i in range(graph.size):
            for j in range(graph.size):
                if graph.adjacencyMatrix[i][j]:
                    if distance[j] > distance[i] + graph.adjacencyMatrix[i][j]:
                        print("Negative cycle",i,j,distance[j],distance[i] + graph.adjacencyMatrix[i][j])

        print(distance)
        assert (distance==[0, 4, 12, 19, 21, 11, 9, 8, 14])

        print(predcesor)


if __name__ == '__main__':
    a = [[0,7,9,0,0,14],
         [7,0,10,15,0,0],
         [9,10,0,11,0,2],
         [0,15,11,0,6,0],
         [0,0,0,6,0,9],
         [14,0,2,0,9,0]]


    a =              [[0, 4, 0, 0, 0, 0, 0, 8, 0],
                      [4, 0, 8, 0, 0, 0, 0, 11, 0],
                      [0, 8, 0, 7, 0, 4, 0, 0, 2],
                      [0, 0, 7, 0, 9, 14, 0, 0, 0],
                      [0, 0, 0, 9, 0, 10, 0, 0, 0],
                      [0, 0, 4, 0, 10, 0, 2, 0, 0],
                      [0, 0, 0, 14, 0, 2, 0, 1, 6],
                      [8, 11, 0, 0, 0, 0, 1, 0, 7],
                      [0, 0, 2, 0, 0, 0, 6, 7, 0]
        ]

    # bad example, with negative edges
    a = [ [0,100,2],
        [100,0,-1],
        [2,-1,0]
        ]

    g = Graph(a)
    print(g)
    s = Solution()
    s.bellmanFordShortestPath(g, 0)




    
