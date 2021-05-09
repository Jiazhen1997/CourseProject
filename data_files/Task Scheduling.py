
__author__ = 'Danyang'


class Solution(object):
    def solve(self, cipher):
        
        tasks = cipher
        tasks.sort(key=lambda t: t[0])

        overshot = -1
        timer = 0
        for task in tasks:
            timer += task[1]
            overshot = max(overshot, timer - task[0])

        return overshot


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""i""m""p""o""r""t"" ""s""y""s""
""
"" "" "" "" ""f"" ""="" ""o""p""e""n""(