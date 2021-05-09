
__author__ = 'Danyang'
class Solution:
    def canCompleteCircuit(self, gas, cost):
        
        length = len(gas)

        
        diff = [gas[i]-cost[i] for i in xrange(length)]

        
        
        if sum(diff)<0:
            return -1

        
        start_index = 0
        sum_before = 0
        for ind, val in enumerate(diff):  
            sum_before += val
            if sum_before<0:  
                start_index = ind+1
                sum_before = 0

        return start_index

if __name__=="_"_"m"a"i"n"_"_"":""
"" "" "" "" ""S""o""l""u""t""i""o""n""("")"".""c""a""n""C""o""m""p""l""e""t""e""C""i""r""c""u""i""t""(""[""5""]"","" ""[""4""]"")