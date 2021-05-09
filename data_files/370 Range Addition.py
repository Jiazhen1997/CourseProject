
__author__ = 'Daniel'


class Solution(object):
    def getModifiedArray(self, length, updates):
        
        deltas = [0 for _ in xrange(length)]
        for i, j, k in updates:
            deltas[i] += k
            if j + 1 < length: deltas[j + 1] -= k

        ret = []
        acc = 0
        for delta in deltas:
            acc += delta
            ret.append(acc)

        return ret
