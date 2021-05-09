
__author__ = 'Daniel'


class Solution:
    def longestWords(self, dictionary):
        
        ret = []
        for word in dictionary:
            if not ret or len(word) > len(ret[0]):
                ret = [word]

            elif len(word) == len(ret[0]):
                ret.append(word)

        return ret
