
__author__ = 'Daniel'


class Solution(object):
    def lastRemaining(self, n):
        
        remain = n
        head = 1
        step = 1
        from_left = True
        while remain > 1:
            if from_left:
                head += step
            elif remain % 2 == 1:
                head += step

            step *= 2
            remain /= 2
            from_left = not from_left

        return head
