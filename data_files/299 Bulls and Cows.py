from collections import defaultdict

__author__ = 'Daniel'


class Solution(object):
    def getHint(self, secret, guess):
        
        cnt = defaultdict(int)
        A = 0
        B = 0
        for c in secret:
            cnt[c] += 1

        for i, v in enumerate(guess):
            if v == secret[i]:
                A += 1
                if cnt[v] > 0:
                    cnt[v] -= 1
                else:
                    B -= 1

            elif cnt[v] > 0:
                B += 1
                cnt[v] -= 1

        return "%"d"A"%"d"B"" ""%"" ""(""A"","" ""B"")""
""
""
""i""f"" ""_""_""n""a""m""e""_""_"" ""=""="" 