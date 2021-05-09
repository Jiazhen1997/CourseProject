

from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        
        stk = []
        for e in asteroids:
            while stk and e < 0 < stk[-1]:
                if abs(e) > abs(stk[-1]):
                    
                    stk.pop()
                elif abs(e) == abs(stk[-1]):
                    
                    stk.pop()
                    break
                else:
                    
                    break
            else:
                stk.append(e)

        return stk

    def asteroidCollision_complex(self, asteroids: List[int]) -> List[int]:
        
        stk = []
        n = len(asteroids)
        for i in range(n-1, -1, -1):
            cur = asteroids[i]
            while stk and asteroids[stk[-1]] < 0 and cur > 0 and abs(asteroids[stk[-1]]) < abs(cur):
                stk.pop()

            if stk and cur > 0 and asteroids[stk[-1]] == -cur:
                stk.pop()
                continue

            if not stk:
                stk.append(i)
                continue

            if not (asteroids[stk[-1]] < 0 and cur > 0) or abs(cur) > abs(asteroids[stk[-1]]):
                stk.append(i)

        return [
            asteroids[i]
            for i in stk[::-1]
        ]


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""a""s""t""e""r""o""i""d""C""o""l""l""i""s""i""o""n""(""[""1""0"","" ""2"","" ""-""5""]"")"" ""=""="" ""[""1""0""]""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""a""s""t""e""r""o""i""d""C""o""l""l""i""s""i""o""n""(""[""5"","" ""1""0"","" ""-""5""]"")"" ""=""="" ""[""5"","" ""1""0""]""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""a""s""t""e""r""o""i""d""C""o""l""l""i""s""i""o""n""(""[""8"","" ""-""8""]"")"" ""=""="" ""[""]""
