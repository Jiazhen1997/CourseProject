



class Solution:
    def findSubsequences(self, nums):
        
        subs = set()
        for n in nums:
            subs |= set([
                sub + (n,)
                for sub in subs
                if n >= sub[-1]
            ])
            subs.add((n,))
            
        return [
            list(sub)
            for sub in subs
            if len(sub) >= 2
        ]


    def findSubsequences(self, nums):
        
        l = len(nums)
        F = [
            [(nums[i],)]
            for i in range(l)
        ]
        ret = set()
        for i in range(1, l):
            for j in range(i):
                if nums[i] >= nums[j]:
                    for t in F[j]:
                        cur = t + (nums[i],)
                        ret.add(cur)
                        F[i].append(cur)

        return list(map(list, ret))
