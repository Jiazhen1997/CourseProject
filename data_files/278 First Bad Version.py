
__author__ = 'Daniel'


def isBadVersion(version):
    pass


class Solution(object):
    def firstBadVersion(self, n):
        
        l = 1
        h = n+1
        while l < h:
            m = (l+h)/2
            if not isBadVersion(m):
                l = m+1
            else:
                h = m

        return l