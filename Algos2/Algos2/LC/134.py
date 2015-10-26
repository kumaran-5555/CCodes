class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """

        start = 0

        n = len(gas)
        while start < n:

            tank = 0
            i = start
            while True:
                tank += gas[i%n]
                tank -= cost[i%n]
                if tank < 0:
                    # could not go to next station
                    # try the next one as start
                    start = i+1
                    break
                else:
                    i += 1

                if i%n == start:
                    # we reachced the starting station
                    return i%n

        return -1













=======
        
>>>>>>> origin/master
