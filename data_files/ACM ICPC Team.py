
__author__ = 'Danyang'


class Solution(object):
    def solve(self, cipher):
        
        N, M, ppl = cipher
        team_cnt = 0
        max_topic = 0
        for i in xrange(N):
            for j in xrange(i + 1, N):
                cnt = self.common_topics(M, ppl[i], ppl[j])
                if cnt == max_topic:
                    team_cnt += 1
                elif cnt > max_topic:
                    team_cnt = 1
                    max_topic = cnt
        return "%"d"\"n"%"d"" ""%"" ""(""m""a""x""_""t""o""p""i""c"","" ""t""e""a""m""_""c""n""t"")""
""
"" "" "" "" ""d""e""f"" ""c""o""m""m""o""n""_""t""o""p""i""c""s""(""s""e""l""f"","" ""M"","" ""a"","" ""b"")"":""
"" "" "" "" "" "" "" "" ""t""o""p""i""c"" ""="" ""a"" ""|"" ""b""
"" "" "" "" "" "" "" "" ""t""o""p""i""c""_""c""n""t"" ""="" ""b""i""n""(""t""o""p""i""c"")"".""c""o""u""n""t""(