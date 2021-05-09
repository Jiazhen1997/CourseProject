

__author__ = 'Daniel'
from collections import defaultdict


class Solution:
    def majorityElement(self, nums):
        
        cnt = defaultdict(int)
        for num in nums:
            if num in cnt:
                cnt[num] += 1
            else:
                if len(cnt) < 3-1:
                    cnt[num] += 1
                else:
                    for k in cnt.keys():
                        cnt[k] -= 1
                        if cnt[k] == 0:
                            del cnt[k]

        ret = []
        for k in cnt.keys():
            if len(filter(lambda x: x == k, nums)) > len(nums)/2:
                ret.append(k)

        return ret

