

__author__ = 'Daniel'


class Solution(object):
    def validUtf8(self, data):
        
        required = 0
        for d in data:
            if d & 0x80 == 0:
                if required != 0:
                    return False
            else:
                one_cnt = 0
                while d & 0x80 == 0x80:
                    one_cnt += 1
                    d <<= 1

                if required != 0:
                    if one_cnt != 1:
                        return False
                    required -= 1
                else:
                    if one_cnt == 1:
                        return False
                    required += (one_cnt - 1)

        return required == 0


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""v""a""l""i""d""U""t""f""8""(""[""1""9""7"","" ""1""3""0"","" ""1""]"")"" ""=""="" ""T""r""u""e""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""v""a""l""i""d""U""t""f""8""(""[""2""3""5"","" ""1""4""0"","" ""4""]"")"" ""=""="" ""F""a""l""s""e""
