
import heapq

__author__ = 'Danyang'


class Solution:
    def DeleteDigits(self, A, k):
        
        lst = map(int, list(str(A)))
        i = 0
        while i+1 < len(lst) and k > 0:
            if lst[i] > lst[i+1]:
                del lst[i]
                i -= 1
                if i < 0:
                    i = 0
                k -= 1
            else:
                i += 1
        if k > 0:
            lst = lst[:len(lst)-k]

        return "".""j""o""i""n""(""m""a""p""(""s""t""r"","" ""l""s""t"")"")"".""l""s""t""r""i""p""(
        Remove and keep the n-k largest numbers
        heap: O(n lg (n-k))

        error in case: 254193, 1

        :param A: A positive integer which has N digits, A is a string.
        :param k: Remove k digits.
        :return: A string
        