
__author__ = 'Daniel'


class Solution(object):
    def findNthDigit(self, n):
        
        digit_cnt = 1
        num_cnt = 9
        while n > digit_cnt * num_cnt:
            n -= digit_cnt * num_cnt
            digit_cnt += 1
            num_cnt *= 10

        n -= 1  
        q, r = n / digit_cnt, n % digit_cnt
        target = num_cnt / 9 + q
        return int(str(target)[r])
