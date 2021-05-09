
__author__ = 'Daniel'





class NestedInteger(object):
    def isInteger(self):
        
        return True

    def getInteger(self):
        
        return 0

    def getList(self):
        
        return []


class NestedIterator(object):
    def __init__(self, nestedList):
        
        self.stk = [[nestedList, 0]]  

    def next(self):
        
        nl, idx = self.stk[-1]
        nxt = nl[idx].getInteger()
        self.stk[-1][1] = idx + 1  
        return nxt

    def hasNext(self):
        
        while self.stk:
            nl, idx = self.stk[-1]
            if idx < len(nl):
                ni = nl[idx]
                if ni.isInteger():
                    return True
                else:
                    self.stk[-1][1] = idx + 1  
                    nxt_nl = ni.getList()
                    self.stk.append([nxt_nl, 0])
            else:
                self.stk.pop()

        return False



class NestedIteratorVerbose(object):
    def __init__(self, nestedList):
        
        self.nl_stk = [nestedList]
        self.idx_stk = [0]

    def next(self):
        
        if self.hasNext():
            nl = self.nl_stk[-1]
            idx = self.idx_stk[-1]
            nxt = nl[idx]
            self.idx_stk[-1] = idx + 1
            return nxt

        raise StopIteration()

    def hasNext(self):
        
        while self.nl_stk:
            nl = self.nl_stk[-1]
            idx = self.idx_stk[-1]
            if idx < len(nl):
                ni = nl[idx]
                if ni.isInteger():
                    return True
                else:
                    self.idx_stk[-1] = idx+1
                    nxt_nl = ni.getList()
                    nxt_idx = 0
                    self.nl_stk.append(nxt_nl)
                    self.idx_stk.append(nxt_idx)
            else:
                self.nl_stk.pop()
                self.idx_stk.pop()

        return False





