

from collections import Counter


class Solution:
    def findAnagrams(self, s, target):
        
        ret = []
        counter_target = Counter(target)
        counter_cur = Counter(s[:len(target)])
        if counter_cur == counter_target:
            ret.append(0)

        for idx in range(len(target), len(s)):
            head = s[idx - len(target)]
            tail = s[idx]
            counter_cur[tail] += 1
            counter_cur[head] -= 1
            if counter_cur[head] == 0:
                del counter_cur[head]  
            if counter_cur == counter_target:
                
                ret.append(idx - len(target) + 1)

        return ret


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""f""i""n""d""A""n""a""g""r""a""m""s""(