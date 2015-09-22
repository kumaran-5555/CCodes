#!/usr/bin/python
__author__ = 'serajago'


class Matrix(list):
    def __init__(self, rows, cols, defaultVal=None):
        self.m = []
        self.rows = rows
        self.cols = cols
        if rows == 1:
            self.m = [defaultVal] * cols
        else:
            for i in range(rows):
                self.m.append([defaultVal] * cols)
    def __str__(self):
        tmp = ""
        if self.rows == 1:
            tmp = str(self.m)
            return  tmp
        for i in range(self.rows):
            tmp = str(self.m[i]) + "\n"
        return  tmp

    def __getitem__(self, item):
        return  self.m[item]

    def __setitem__(self, key, value):
        self.m[key] = value








