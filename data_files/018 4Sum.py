
__author__ = 'Danyang'
class Solution:
    def fourSum_TLE(self, num, target):
        

        
        result = []
        num.sort()
        length = len(num)

        h = 0
        while h<length-3:
            i = h+1
            while i<length-2:
                j = i+1
                k = length-1
                while j<k:
                    lst = [num[h], num[i], num[j], num[k]]
                    summation = sum(lst)
                    if summation==target:
                        result.append(lst)
                        k -= 1
                        j += 1
                        
                        while j<k and num[j]==num[j-1]:
                            j += 1
                        while j<k and num[k]==num[k+1]:
                            k -= 1
                    elif summation>target:
                        k -= 1
                    else:
                        j += 1
    
                i += 1
                
                while i<length-2 and num[i]==num[i-1]:
                    i += 1
            h += 1
            
            while h<length-3 and num[h]==num[h-1]:
                h += 1

        return result

    def fourSum(self, num, target):
        
        length, result_set, sum2index = len(num), set(), {}
        if length<4:
            return []
        num.sort()

        for p in xrange(length):
            for q in xrange(p+1, length):
                
                if num[p]+num[q] not in sum2index:
                    sum2index[num[p]+num[q]] = [(p, q)]
                else:
                    sum2index[num[p]+num[q]].append((p, q))

        for i in xrange(length):
            for j in xrange(i+1, length-2):
                sum_remain = target-num[i]-num[j]
                if sum_remain in sum2index:
                    
                    for pair in sum2index[sum_remain]:
                        if pair[0]>j:  
                            result_set.add(( num[i], num[j], num[pair[0]], num[pair[1]] ))

        return [list(i) for i in result_set]  