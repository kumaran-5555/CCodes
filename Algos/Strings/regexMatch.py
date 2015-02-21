#!/usr/bin/python3
__author__ = 'kumaran'
#https://oj.leetcode.com/problems/regular-expression-matching/


class Solution():

    def returnStatus(self, status, cache, key):
        cache[key] = status
        return status

    def regexMatch(self, sPosition, string, rPosition, regex, cache):


        key = ("%d_%d")%(sPosition, rPosition)
        if key in cache:
            return cache[key]

        if sPosition == len(string) and rPosition == len(regex):
            # we consumed all
            return self.returnStatus(True, cache, key)
        if sPosition < len(string) and rPosition == len(regex):
            # consumed regex but not string
            return self.returnStatus(False, cache,key)

        if regex[rPosition] == '.':
            match = 'ANY'
        else:
            match = 'CHAR'
            char = regex[rPosition]

        if rPosition < len(regex)-1:
            if regex[rPosition+1] == '*':
                match = 'STAR'
                char = regex[rPosition]



        if match == 'ANY':
            if sPosition == len(string):
                return self.returnStatus(False, cache, key)

            # consume one char and recurse
            status = self.regexMatch(sPosition+1,string, rPosition+1, regex, cache)
            return self.returnStatus(status, cache, key)

        elif match == 'CHAR':
            if sPosition == len(string):
                return self.returnStatus(False, cache, key)
            # consume one char if matches and recurse
            if string[sPosition] == char:
                status = self.regexMatch(sPosition+1, string, rPosition+1, regex, cache)
                return self.returnStatus(status, cache, key)
            else:
                return self.returnStatus(False, cache, key)

        elif match == 'STAR':
            if sPosition == len(string) and rPosition == len(regex)-2:
                # what is left out is only star regex
                return self.returnStatus(True, cache, key)
            elif sPosition == len(string):
                # we can only try zero matchings
                # what might be left is unkown, so just proceed consuming only star and recurse
                status = self.regexMatch(sPosition, string, rPosition+2, regex, cache)
                return self.returnStatus(status, cache,key)

            # comes here when string has more chars
            # try matching zero times
            status = self.regexMatch(sPosition, string, rPosition+2, regex, cache)
            if status:
                return self.returnStatus(status, cache, key)


            # if char matches, match one and recurs
            if (char != '.' and string[sPosition] == char) or (char == '.'):
                # consume once and recurs
                status = self.regexMatch(sPosition+1, string, rPosition, regex, cache)
                return self.returnStatus(status, cache,key)
            else:
                return self.returnStatus(False, cache, key)


            # consume zero timess nad recurs

    def isMatch(self, s, p):
        cache = {}
        return self.regexMatch(0, s, 0, p, cache)

if __name__ == '__main__':
    s = Solution()
    #print(s.isMatch("ab",".*"))
    #print(s.isMatch("aaaaaaaaaaaaab", "a*a*a*a*a*a*a*a*a*a*c"))
    #print(s.isMatch("ab",".*c"))
    print(s.isMatch("","c*c*"))
    
