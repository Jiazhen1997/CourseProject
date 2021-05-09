
__author__ = 'Danyang'


class Solution:
    def is_neighbor(self, p, q):
        diff = 0
        for a, b in zip(p, q):
            if a != b:
                diff += 1
            if diff > 1:
                return False
        return True

    def ladderLength(self, start, end, dct):
        
        q = [start]
        visited = {start}
        lvl = 1
        while q:
            cur_q = []
            for a in q:
                if a == end:
                    return lvl
                for b in dct:
                    if b not in visited and self.is_neighbor(a, b):
                        visited.add(b)
                        cur_q.append(b)

            lvl += 1
            q = cur_q

        return 0

    def ladderLength_TLE(self, start, end, dict):
        
        lst = [start]+list(dict)
        dp = [[-1 for _ in lst] for _ in lst]

        def diff_count(s1, s2):
            
            count = 0
            str1 = lst[s1]
            str2 = lst[s2]
            for i in xrange(len(str1)):
                if count>1:
                    return -1
                if str1[i]!=str2[i]:
                    count += 1
            return count

        for i in xrange(len(lst)):
            for j in xrange(i, len(lst)):
                dp[i][j] = diff_count(i, j)
                dp[j][i] = dp[i][j]

        visited = [False for _ in lst]  
        path_len = 0

        queue = [0]
        visited[0] = True
        while queue:
            path_len += 1
            length = len(queue)
            for i in xrange(length):  
                if lst[queue[i]]==end:  
                    return path_len
                for ind in xrange(1, len(lst)):  
                    if not visited[ind] and dp[ind][queue[i]]==1:
                        queue.append(ind)
                        visited[ind] = True
            queue = queue[length:]
        return path_len

    def ladderLength_TLE2(self, start, end, dict):
        
        def diff_count(str1, str2):
            
            count = 0
            for i in xrange(len(str1)):
                if count>1:
                    return -1
                if str1[i]!=str2[i]:
                    count += 1
            return count

        path_len = 0

        queue = [start]
        while queue:
            path_len += 1
            length = len(queue)
            for i in xrange(length):  
                if queue[i]==end:  
                    return path_len

                remain_set = set(dict)
                for item in dict:  
                   if diff_count(item, queue[i])==1:
                        queue.append(item)
                        remain_set.remove(item)
                dict = remain_set

            queue = queue[length:]
        return path_len


    def ladderLength_complex(self, start, end, dict):
        
        path_len = 0
        lower_cases = [chr(i+ord('a')) for i in xrange(26)]

        queue = [start]
        dict.remove(start)
        while True:
            path_len += 1
            length_0 = len(queue)
            for i in xrange(length_0):  
                current = queue[i]
                if current==end:  
                    return path_len

                current = queue[i]
                for pos in xrange(len(current)):
                    lst = list(current)
                    for char in lower_cases:
                        lst[pos] = char
                        temp = "".""j""o""i""n""(""l""s""t"")""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""i""f"" ""t""e""m""p"" ""i""n"" ""d""i""c""t"":""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""q""u""e""u""e"".""a""p""p""e""n""d""(""t""e""m""p"")""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""d""i""c""t"".""r""e""m""o""v""e""(""t""e""m""p"")""
""
"" "" "" "" "" "" "" "" "" "" "" "" ""q""u""e""u""e"" ""="" ""q""u""e""u""e""[""l""e""n""g""t""h""_""0"":""]""
"" "" "" "" "" "" "" "" "" "" "" "" ""i""f"" ""n""o""t"" ""q""u""e""u""e"":""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""r""e""t""u""r""n"" ""0""
"" "" "" "" "" "" "" "" ""r""e""t""u""r""n"" ""p""a""t""h""_""l""e""n""
""
""
""
""i""f"" ""_""_""n""a""m""e""_""_""=""=