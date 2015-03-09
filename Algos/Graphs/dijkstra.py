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
    def dijkstraShortestPath(self, graph, sourceIdx):
        # initialize
        priorityQueue = []
        predcesor = {}
        completed = [False] * graph.size
        distance = [float("inf")] * graph.size
        distance[sourceIdx] = 0
        predcesor[sourceIdx] = None


        mapToHeap = {}
        mapToHeap[sourceIdx] = [0, sourceIdx, False]
        heapq.heappush(priorityQueue, mapToHeap[sourceIdx])


        # entry of priority queue entry has [priority, node, isRemoved]

        while len(priorityQueue):
            minEntry = heapq.heappop(priorityQueue)
            if minEntry[-1] == True:
                continue

            u = minEntry[1]
            completed[u] = True
            #print(minEntry)
            for i in range(graph.size):
                if graph.adjacencyMatrix[u][i]:
                    v = i
                    # edge present between u and v
                    if distance[v] > distance[u] + graph.adjacencyMatrix[u][i]:
                        if completed[v] is True:
                            print("Negative path found betwee %d and %d"%(u,v))
                            continue

                        distance[v] = distance[u] + graph.adjacencyMatrix[u][i]
                        predcesor[v] = u
                        # if v is already in heap, make to it removed
                        if v in mapToHeap:
                            mapToHeap[v][2] = True

                        # add new entry to heap
                        mapToHeap[v] = [[distance[v]], v, False]
                        heapq.heappush(priorityQueue, mapToHeap[v])

        print('distance vector '+str(distance))
        print('parent dict '+str(predcesor))





if __name__ == '__main__':
    a = [[0,7,9,0,0,14],
         [7,0,10,15,0,0],
         [9,10,0,11,0,2],
         [0,15,11,0,6,0],
         [0,0,0,6,0,9],
         [14,0,2,0,9,0]]
    '''
    a =  [[0, 4, 0, 0, 0, 0, 0, 8, 0],
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
        [100,0,-1000],
        [2,-1000,0]
        ]
    '''
    g = Graph(a)
    print(g)
    s = Solution()
    s.dijkstraShortestPath(g, 0)




