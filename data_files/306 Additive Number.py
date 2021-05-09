
__author__ = 'Daniel'


class Solution(object):
    def isAdditiveNumber(self, num):
        
        n = len(num)
        for i in xrange(1, n):
            for j in xrange(i, n):
                if self.predicate(num, 0, i, j):
                    return True

        return False

    def predicate(self, s, b, i, j):
        n1 = s[b:i]
        n2 = s[i:j]

        if b != 0 and j == len(s):
            return True
        if not n1 or not n2:
            return False
        if len(n1) > 1 and n1[0] == '0' or len(n2) > 1 and n2[0] == '0':
            return False

        n3 = str(int(n1)+int(n2))
        J = j+len(n3)
        if s[j:J] == n3:
            return self.predicate(s, i, j, J)


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""i""s""A""d""d""i""t""i""v""e""N""u""m""b""e""r""(