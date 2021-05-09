

from typing import List


class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        
        n = len(nums)
        
        
        median = list(sorted(nums))[n//2]

        
        odd = 1
        even = n - 1 if (n - 1) % 2 == 0 else n - 2
        i = 0
        while i < n:
            if nums[i] < median:
                if i >= even and i % 2 == 0:
                    i += 1
                    continue
                nums[i], nums[even] = nums[even], nums[i]
                even -= 2

            elif nums[i] > median:
                if i <= odd  and i % 2 == 1:
                    i += 1
                    continue
                nums[i], nums[odd] = nums[odd], nums[i]
                odd += 2
            else:
                i += 1

    def find_kth(self, A, lo, hi, k):
        p = self.pivot(A, lo, hi)
        if k == p:
            return p
        elif k > p:
            return self.find_kth(A, p + 1, hi, k)
        else:
            return self.find_kth(A, lo, p, k)

    def pivot(self, A, lo, hi):
        
        p = lo
        closed = lo
        for i in range(lo + 1, hi):
            if A[i] < A[p]:
                closed += 1
                A[closed], A[i] = A[i], A[closed]

        A[closed], A[p] = A[p], A[closed]
        return closed


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""S""o""l""u""t""i""o""n""("")"".""w""i""g""g""l""e""S""o""r""t""(""[""1"","" ""5"","" ""1"","" ""1"","" ""6"","" ""4""]"")""
