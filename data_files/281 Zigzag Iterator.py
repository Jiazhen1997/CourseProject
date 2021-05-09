
__author__ = 'Daniel'


class ZigzagIterator(object):
    def __init__(self, v1, v2):
        
        self.mat = [v1, v2]
        self.maxa = max((c, r) for r, c in enumerate(map(lambda x: len(x)-1, self.mat)))
        self.i = 0
        self.j = 0
        self._reposition()

    def _reposition(self):
        while self.i >= len(self.mat) or self.j >= len(self.mat[self.i]):
            if not self.hasNext():
                return

            elif self.i >= len(self.mat):
                self.i = 0
                self.j += 1

            elif self.j >= len(self.mat[self.i]):
                self.i += 1

    def next(self):
        
        if not self.hasNext():
            raise StopIteration

        ret = self.mat[self.i][self.j]
        self.i += 1
        self._reposition()
        return ret

    def hasNext(self):
        
        return self.j <= self.maxa[0]


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""v""1"" ""="" ""[""1"","" ""2""]""
"" "" "" "" ""v""2"" ""="" ""[""3"","" ""4"","" ""5"","" ""6""]""
"" "" "" "" ""i""t""r"" ""="" ""Z""i""g""z""a""g""I""t""e""r""a""t""o""r""(""v""1"","" ""v""2"")""
"" "" "" "" ""w""h""i""l""e"" ""i""t""r"".""h""a""s""N""e""x""t""("")"":""
"" "" "" "" "" "" "" "" ""p""r""i""n""t"" ""i""t""r"".""n""e""x""t""("")