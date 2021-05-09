

import bisect


class Solution:
    def findRadius(self, houses, heaters):
        
        houses.sort()
        heaters.sort()
        r = 0
        i = 0
        for h in houses:
            i = bisect.bisect(heaters, h)  
            left = max(0, i - 1)
            right = min(len(heaters) - 1, i)
            r_cur = min(abs(heaters[left] - h), abs(heaters[right] - h))
            r = max(r, r_cur)
            
        return r

    def findRadius_naive(self, houses, heaters):
        
        houses.sort()
        heaters.sort()
        heaters.append(float('inf'))
        r = 0
        i = 0
        for h in houses:
            
            while h > (heaters[i] + heaters[i+1]) / 2:
                
                i += 1

            r = max(r, abs(heaters[i] - h))

        return r


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""f""i""n""d""R""a""d""i""u""s""(""[""1"",""2"",""3"",""4""]"","" ""[""1"",""4""]"")"" ""=""="" ""1""
