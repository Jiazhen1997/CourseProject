
__author__ = 'Daniel'


class Solution(object):
    def countBits(self, num):
        
        ret = [0]
        i = 0
        hi = len(ret)
        while len(ret) < num + 1:
            if i == hi:
                i = 0
                hi = len(ret)

            ret.append(1+ret[i])
            i += 1

        return ret
