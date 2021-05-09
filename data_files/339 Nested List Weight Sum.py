
__author__ = 'Daniel'





class NestedInteger(object):
    def isInteger(self):
        

    def getInteger(self):
        

    def getList(self):
        


class Solution(object):
    def __init__(self):
        self.sum = 0

    def depthSum(self, nestedList):
        
        for elt in nestedList:
            self.dfs(elt, 1)

        return self.sum

    def dfs(self, ni, depth):
        if ni.isInteger():
            self.sum += ni.getInteger() * depth
        else:
            lst = ni.getList()
            for elt in lst:
                self.dfs(elt, depth + 1)
