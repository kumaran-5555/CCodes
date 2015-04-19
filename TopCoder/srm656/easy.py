__author__ = 'serajago'

import string
class CorruptedMessage:
    def reconstructMessage(self, s, k):
        n = len(s)
        for i in string.ascii_lowercase:
            original = i*n
            diff = 0
            for j in range(n):
                if s[j] != original[j]:
                    diff += 1
            if diff == k:
                return original





