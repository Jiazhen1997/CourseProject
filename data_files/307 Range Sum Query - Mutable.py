

__author__ = 'Daniel'


class BinaryIndexTree(object):
    def __init__(self, nums):
        
        n = len(nums)
        self.nums = [0 for _ in xrange(n+1)]
        self.N = [0 for _ in xrange(n+1)]
        for i, v in enumerate(nums):
            self.set(i+1, v)

    def _lowbit(self, a):
        return a & -a

    def set(self, i, val):
        diff = val - self.nums[i]
        self.nums[i] = val
        while i < len(self.N):
            self.N[i] += diff
            i += self._lowbit(i)

    def get(self, i):
        ret = 0
        while i > 0:
            ret += self.N[i]
            i -= self._lowbit(i)

        return ret


class NumArray(object):
    def __init__(self, nums):
        
        self.bit = BinaryIndexTree(nums)

    def update(self, i, val):
        
        self.bit.set(i+1, val)

    def sumRange(self, i, j):
        
        return self.bit.get(j+1)-self.bit.get(i)