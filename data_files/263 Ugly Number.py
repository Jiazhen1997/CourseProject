
__author__ = 'Daniel'


class Solution(object):
    def isUgly(self, num):
        
        if num < 1:
            return False
        if num == 1:
            return True

        ugly = {2, 3, 5}

        prime = 2
        while prime*prime <= num and num > 1:
            if num % prime != 0:
                prime += 1
            else:
                num /= prime
                if prime not in ugly:
                    return False

        if num not in ugly:
            return False

        return True