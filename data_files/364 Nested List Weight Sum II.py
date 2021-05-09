
__author__ = 'Daniel'





class NestedInteger(object):
    def __init__(self, value=None):
        

    def isInteger(self):
        

    def add(self, elem):
        

    def setInteger(self, value):
        

    def getInteger(self):
        

    def getList(self):
        


class Solution(object):
    def __init__(self):
        self.sum = 0

    def depthSumInverse(self, nestedList):
        
        inv_depth = self.height(nestedList)
        self.inverseDepthSum(nestedList, inv_depth)
        return self.sum

    def height(self, nl):
        nl_lst = filter(lambda x: not x.isInteger(), nl)
        if not nl_lst:
            return 1
        if nl_lst:
            return 1 + max(
                map(lambda x: self.height(x.getList()), nl_lst)
            )

    def inverseDepthSum(self, nl, inv_depth):
        nl_lst = filter(lambda x: not x.isInteger(), nl)
        ni_list = filter(lambda x: x.isInteger(), nl)
        if nl_lst:
            map(lambda x: self.inverseDepthSum(x.getList(), inv_depth - 1), nl_lst)
        if ni_list:
            self.sum += sum(map(lambda x: x.getInteger() * inv_depth, ni_list))


class SolutionError(object):
    def __init__(self):
        self.sum = 0

    def depthSumInverse(self, nestedList):
        
        self.dfs(nestedList)
        return self.sum

    def dfs(self, nl):
        
        height = 1

        nl_lst = filter(lambda x: not x.isInteger(), nl)
        ni_list = filter(lambda x: x.isInteger(), nl)
        if nl_lst:
            height = 1 + max(
                map(lambda x: self.dfs(x.getList()), nl_lst)
            )
        if ni_list:
            self.sum += sum(map(lambda x: x.getInteger() * height, ni_list))

        return height
