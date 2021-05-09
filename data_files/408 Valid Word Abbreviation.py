
__author__ = 'Daniel'


class Solution(object):
    def validWordAbbreviation(self, word, abbr):
        
        w = 0
        a = 0
        while w < len(word) and a < len(abbr):
            if abbr[a].isdigit() and abbr[a] != '0':
                e = a
                while e < len(abbr) and abbr[e].isdigit(): e += 1
                num = int(abbr[a:e])
                a = e
                w += num
            else:
                if word[w] != abbr[a]:
                    return False

                w += 1
                a += 1

        return w == len(word) and a == len(abbr)


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""v""a""l""i""d""W""o""r""d""A""b""b""r""e""v""i""a""t""i""o""n""(