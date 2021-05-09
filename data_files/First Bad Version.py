
__author__ = 'Danyang'


class VersionControl:
    @classmethod
    def isBadVersion(cls, id):
        return True


class Solution:
    def findFirstBadVersion(self, n):
        
        l = 1
        h = n+1
        while l < h:
            m = (l+h)/2
            if not VersionControl.isBadVersion(m):
                l = m+1
            else:
                h = m

        return l


