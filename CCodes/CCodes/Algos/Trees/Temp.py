#!/usr/bin/python3
__author__ = 'kumaran'
import math

class Solution():
    def __init__(self):
        self.wMax = 1000
        self.c = 0.4
        self.b = 0.8
        self.t = 0

    def tcpCubicSimulate(self):
        while True:
            self.k = ((self.wMax * self.b ) / self.c ) ** (1/3)
            currWindow = self.c * ((self.t - self.k ) ** 3) + self.wMax
            print(("%f\t%f\t%f") %(self.t, self.k, currWindow))
            self.t += 0.5

            if currWindow > self.wMax * 2:
                break


if __name__ == '__main__':
    s = Solution()

    s.tcpCubicSimulate()
