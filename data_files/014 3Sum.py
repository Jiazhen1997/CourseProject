
__author__ = 'Danyang'


class Solution:
    def threeSum_duplicate(self, num):
        
        reverse_map = {}
        for ind, val in enumerate(num):
            if val not in reverse_map:
                reverse_map[val] = [ind]
            else:
                reverse_map[val].append(ind)

        result = []
        for i in xrange(len(num)):
            for j in xrange(i, len(num)):
                target = 0-num[i]-num[j]
                if target not in reverse_map:
                    continue
                for index in reverse_map[target]:
                    if i != index and j != index:
                        result.append([num[i], num[j], target])
                        break
        return result

    def threeSum_TLE(self, num):
        

        
        reverse_map = {}
        for ind, val in enumerate(num):
            if val not in reverse_map:
                reverse_map[val] = [ind]
            else:
                reverse_map[val].append(ind)

        result = {}
        for i in xrange(len(num)):
            for j in xrange(i, len(num)):
                target = 0-num[i]-num[j]
                if target not in reverse_map:
                    continue
                for index in reverse_map[target]:
                    if index != i and index != j:
                        lst = sorted([num[i], num[j], target])
                        lst = tuple(lst)
                        result[lst] = 1  
                        break

        return result.keys()

    def threeSum(self, num):
        

        
        result = []
        num.sort()  
        i = 0
        while i < len(num)-2:
            j = i+1
            k = len(num)-1
            while j < k:
                lst = [num[i], num[j], num[k]]
                if sum(lst) == 0:
                    result.append(lst)
                    k -= 1
                    j += 1
                    
                    while j < k and num[j] == num[j-1]:
                        j += 1
                    while j < k and num[k] == num[k+1]:
                        k -= 1
                elif sum(lst) > 0:
                    k -= 1
                else:
                    j += 1

            i += 1
            
            while i < len(num)-2 and num[i] == num[i-1]:
                i += 1

        return result


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""p""r""i""n""t"" ""S""o""l""u""t""i""o""n""("")"".""t""h""r""e""e""S""u""m""(""[""-""1"","" ""0"","" ""1"","" ""2"","" ""-""1"","" ""-""4""]"")