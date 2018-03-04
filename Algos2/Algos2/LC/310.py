from collections import defaultdict

class Solution:
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        
        nodes = n
        if nodes == 1:
            return [0]
        
        dToN = defaultdict(set)
        es = defaultdict(set)
        nToD = defaultdict(lambda : 0)

        for e in edges:
            es[e[0]].add(e[1])
            es[e[1]].add(e[0])
            nToD[e[0]] += 1 
            nToD[e[1]] += 1

        for node in nToD:
            dToN[nToD[node]].add(node)

        '''
        keep removing leafs until the remaining tree has
        either 1 node or two nodes

        make sure leafs are removed in one time step i.e. during a removal 
        iteration we don't want to considered a newly created leaf in the same iteration

        '''
        while nodes > 2:
            # leafs 
            leafs = list(dToN[1])
            for n in leafs:
                for m in es[n]:
                    d = nToD[m]
                    dToN[d].remove(m)
                    dToN[d-1].add(m)
                    nToD[m] = d-1
                    es[m].remove(n)

                del nToD[n]
                dToN[1].remove(n)                                    
                nodes -= 1

        return list(nToD.keys())

if __name__ == '__main__':
    c = Solution()
    print(c.findMinHeightTrees(6,  [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]] ))
