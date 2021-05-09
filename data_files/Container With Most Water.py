
__author__ = 'Daniel'


class Solution(object):
    def maxArea(self, H):
        maxa = 0
        s = 0
        e = len(H) - 1
        while s < e:
            maxa = max(maxa, min(H[s], H[e])*(e-s))
            if H[s] < H[e]:
                s += 1
            else:
                e -= 1

        return maxa


