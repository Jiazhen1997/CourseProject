
__author__ = 'Danyang'

class Solution_MLE:  
    class Node:
        def __init__(self, string, pre, dict):
            self.string = string
            self.pre = pre  
            self.dict = dict

        def __repr__(self):
            return repr(self.string)

    def findLadders(self, start, end, dict):
        

        result = []
        lower_cases = [chr(i+ord('a')) for i in xrange(26)]

        start_node = self.Node(start, None, dict-{start}|{end})
        queue = [start_node]
        while queue:
            length_0 = len(queue)
            for i in xrange(length_0):  
                current = queue[i]
                if current.string==end:  
                    self.append(current, result)
            if result:  
                return result

            for i in xrange(length_0):
                current = queue[i].string
                for pos in xrange(len(current)):
                    lst = list(current)
                    for char in lower_cases:
                        lst[pos] = char
                        temp = "".""j""o""i""n""(""l""s""t"")""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""i""f"" ""t""e""m""p"" ""i""n"" ""q""u""e""u""e""[""i""]"".""d""i""c""t"":""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""q""u""e""u""e"".""a""p""p""e""n""d""(""s""e""l""f"".""N""o""d""e""(""t""e""m""p"","" ""q""u""e""u""e""[""i""]"","" ""q""u""e""u""e""[""i""]"".""d""i""c""t""-""{""t""e""m""p""}"")"")""
""
"" "" "" "" "" "" "" "" "" "" "" "" ""q""u""e""u""e"" ""="" ""q""u""e""u""e""[""l""e""n""g""t""h""_""0"":""]""
"" "" "" "" "" "" "" "" ""r""e""t""u""r""n"" ""[""]"" "" ""#"" ""n""a""t""u""r""a""l"" ""b""r""e""a""k"","" ""n""o"" ""r""e""s""u""l""t""
""
"" "" "" "" ""d""e""f"" ""a""p""p""e""n""d""(""s""e""l""f"","" ""n""o""d""e"","" ""r""e""s""u""l""t"")"":""
"" "" "" "" "" "" "" "" ""c""u""r"" ""="" ""n""o""d""e""
"" "" "" "" "" "" "" "" ""l""s""t"" ""="" ""[""]""
"" "" "" "" "" "" "" "" ""w""h""i""l""e"" ""c""u""r"":""
"" "" "" "" "" "" "" "" "" "" "" "" ""l""s""t"".""i""n""s""e""r""t""(""0"","" ""c""u""r"".""s""t""r""i""n""g"")""
"" "" "" "" "" "" "" "" "" "" "" "" ""c""u""r"" ""="" ""c""u""r"".""p""r""e""
"" "" "" "" "" "" "" "" ""r""e""s""u""l""t"".""a""p""p""e""n""d""(""l""s""t"")""
""
""
""c""l""a""s""s"" ""S""o""l""u""t""i""o""n""_""T""L""E"":""
"" "" "" "" ""c""l""a""s""s"" ""N""o""d""e"":""
"" "" "" "" "" "" "" "" ""d""e""f"" ""_""_""i""n""i""t""_""_""(""s""e""l""f"","" ""s""t""r""i""n""g"","" ""p""r""e"")"":""
"" "" "" "" "" "" "" "" "" "" "" "" ""s""e""l""f"".""s""t""r""i""n""g"" ""="" ""s""t""r""i""n""g""
"" "" "" "" "" "" "" "" "" "" "" "" ""s""e""l""f"".""p""r""e"" ""="" ""p""r""e"" "" ""#"" ""n""o""d""e""
""
"" "" "" "" "" "" "" "" ""d""e""f"" ""_""_""r""e""p""r""_""_""(""s""e""l""f"")"":""
"" "" "" "" "" "" "" "" "" "" "" "" ""r""e""t""u""r""n"" ""r""e""p""r""(""s""e""l""f"".""s""t""r""i""n""g"")""
""
"" "" "" "" ""d""e""f"" ""f""i""n""d""L""a""d""d""e""r""s""(""s""e""l""f"","" ""s""t""a""r""t"","" ""e""n""d"","" ""d""i""c""t"")"":""
"" "" "" "" "" "" "" "" 
        dict |= {end}
        result = []
        lower_cases = [chr(i+ord('a')) for i in xrange(26)]

        start_node = self.Node(start, None)
        queue = [start_node]
        while queue:
            length_0 = len(queue)
            for i in xrange(length_0):  
                current = queue[i]
                if current.string==end:  
                    self.append(current, result)
            if result:  
                return result

            for i in xrange(length_0):
                current = queue[i].string
                for pos in xrange(len(current)):
                    lst = list(current)
                    for char in lower_cases:
                        lst[pos] = char
                        temp = "".""j""o""i""n""(""l""s""t"")""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""i""f"" ""t""e""m""p"" ""i""n"" ""d""i""c""t"" ""a""n""d"" ""n""o""t"" ""s""e""l""f"".""i""n""_""p""r""e""v""i""o""u""s""(""q""u""e""u""e""[""i""]"","" ""t""e""m""p"")"":""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""q""u""e""u""e"".""a""p""p""e""n""d""(""s""e""l""f"".""N""o""d""e""(""t""e""m""p"","" ""q""u""e""u""e""[""i""]"")"")""
""
"" "" "" "" "" "" "" "" "" "" "" "" ""q""u""e""u""e"" ""="" ""q""u""e""u""e""[""l""e""n""g""t""h""_""0"":""]""
"" "" "" "" "" "" "" "" ""r""e""t""u""r""n"" ""[""]"" "" ""#"" ""n""a""t""u""r""a""l"" ""b""r""e""a""k"","" ""n""o"" ""r""e""s""u""l""t""
""
"" "" "" "" ""d""e""f"" ""a""p""p""e""n""d""(""s""e""l""f"","" ""n""o""d""e"","" ""r""e""s""u""l""t"")"":""
"" "" "" "" "" "" "" "" ""c""u""r"" ""="" ""n""o""d""e""
"" "" "" "" "" "" "" "" ""l""s""t"" ""="" ""[""]""
"" "" "" "" "" "" "" "" ""w""h""i""l""e"" ""c""u""r"":""
"" "" "" "" "" "" "" "" "" "" "" "" ""l""s""t"".""i""n""s""e""r""t""(""0"","" ""c""u""r"".""s""t""r""i""n""g"")""
"" "" "" "" "" "" "" "" "" "" "" "" ""c""u""r"" ""="" ""c""u""r"".""p""r""e""
"" "" "" "" "" "" "" "" ""r""e""s""u""l""t"".""a""p""p""e""n""d""(""l""s""t"")""
""
"" "" "" "" ""d""e""f"" ""i""n""_""p""r""e""v""i""o""u""s""(""s""e""l""f"","" ""n""o""d""e"","" ""s""t""r""i""n""g"")"":""
"" "" "" "" "" "" "" "" ""c""u""r"" ""="" ""n""o""d""e""
"" "" "" "" "" "" "" "" ""w""h""i""l""e"" ""c""u""r"":""
"" "" "" "" "" "" "" "" "" "" "" "" ""i""f"" ""c""u""r"".""s""t""r""i""n""g""=""=""s""t""r""i""n""g"":""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""r""e""t""u""r""n"" ""T""r""u""e""
"" "" "" "" "" "" "" "" "" "" "" "" ""c""u""r"" ""="" ""c""u""r"".""p""r""e""
"" "" "" "" "" "" "" "" ""r""e""t""u""r""n"" ""F""a""l""s""e""
""
""
""c""l""a""s""s"" ""N""o""d""e"":""
"" "" "" "" ""d""e""f"" ""_""_""i""n""i""t""_""_""(""s""e""l""f"","" ""s""t""r""i""n""g"","" ""p""r""e"")"":""
"" "" "" "" "" "" "" "" ""s""e""l""f"".""s""t""r""i""n""g"" ""="" ""s""t""r""i""n""g""
"" "" "" "" "" "" "" "" ""s""e""l""f"".""p""r""e"" ""="" ""p""r""e"" "" ""#"" ""n""o""d""e""
"" "" "" "" "" "" "" "" ""#"" ""s""e""l""f"".""p""r""e""s"" ""="" ""s""e""l""f"".""p""r""e"".""p""r""e""s""|""{""s""t""r""i""n""g""}"" ""i""f"" ""s""e""l""f"".""p""r""e"" ""e""l""s""e"" ""{""s""t""r""i""n""g""}"" "" ""#"" ""a""c""c""e""l""e""r""a""t""e"" ""s""p""e""e""d""
""
"" "" "" "" ""d""e""f"" ""_""_""r""e""p""r""_""_""(""s""e""l""f"")"":""
"" "" "" "" "" "" "" "" ""r""e""t""u""r""n"" ""r""e""p""r""(""s""e""l""f"".""s""t""r""i""n""g"")""
""
""c""l""a""s""s"" ""S""o""l""u""t""i""o""n""_""T""L""E""2"":""
"" "" "" "" ""d""e""f"" ""f""i""n""d""L""a""d""d""e""r""s""(""s""e""l""f"","" ""s""t""a""r""t"","" ""e""n""d"","" ""d""i""c""t"")"":""
"" "" "" "" "" "" "" "" 
        dict |= {end}  
        result = []
        lower_cases = 'abcdefghijklmnopqrstuvwxyz'

        
        queue = [Node(start, None)]
        while queue:
            length_0 = len(queue)
            for i in xrange(length_0):  
                current = queue[i]

                
                
                dict -= {current.string}

                
                if current.string==end:  
                    self.append(current, result)

            if result:  
                return result

            for i in xrange(length_0):
                current = queue[i].string
                for pos in xrange(len(current)):
                    lst = list(current)
                    for char in lower_cases:
                        lst[pos] = char
                        temp = "".""j""o""i""n""(""l""s""t"")""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""i""f"" ""t""e""m""p"" ""i""n"" ""d""i""c""t"":""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""q""u""e""u""e"".""a""p""p""e""n""d""(""N""o""d""e""(""t""e""m""p"","" ""q""u""e""u""e""[""i""]"")"")""
""
"" "" "" "" "" "" "" "" "" "" "" "" ""q""u""e""u""e"" ""="" ""q""u""e""u""e""[""l""e""n""g""t""h""_""0"":""]""
"" "" "" "" "" "" "" "" ""r""e""t""u""r""n"" ""[""]"" "" ""#"" ""n""a""t""u""r""a""l"" ""b""r""e""a""k"","" ""n""o"" ""r""e""s""u""l""t""
""
"" "" "" "" ""d""e""f"" ""a""p""p""e""n""d""(""s""e""l""f"","" ""n""o""d""e"","" ""r""e""s""u""l""t"")"":""
"" "" "" "" "" "" "" "" ""c""u""r"" ""="" ""n""o""d""e""
"" "" "" "" "" "" "" "" ""l""s""t"" ""="" ""[""]""
"" "" "" "" "" "" "" "" ""w""h""i""l""e"" ""c""u""r"":""
"" "" "" "" "" "" "" "" "" "" "" "" ""l""s""t"".""i""n""s""e""r""t""(""0"","" ""c""u""r"".""s""t""r""i""n""g"")""
"" "" "" "" "" "" "" "" "" "" "" "" ""c""u""r"" ""="" ""c""u""r"".""p""r""e""
"" "" "" "" "" "" "" "" ""r""e""s""u""l""t"".""a""p""p""e""n""d""(""l""s""t"")""
""
""c""l""a""s""s"" ""S""o""l""u""t""i""o""n"":"" "" ""#"" ""u""s""e"" ""s""e""t"" ""t""o"" ""m""i""m""i""c"" ""q""u""e""u""e"","" ""f""a""s""t""e""s""t""
"" "" "" "" ""d""e""f"" ""f""i""n""d""L""a""d""d""e""r""s""(""s""e""l""f"","" ""s""t""a""r""t"","" ""e""n""d"","" ""d""i""c""t"")"":""
"" "" "" "" "" "" "" "" 
        dict |= {start}
        dict |= {end}
        result=[]

        prevMap={}  
        for i in dict:
            prevMap[i]=[]

        candidates=[set(), set()]  
        current=0
        previous=1

        candidates[current].add(start)
        while end not in candidates[current]:
            current, previous = previous, current
            for i in candidates[previous]: dict -= {i}  

            candidates[current].clear()  
            for word in candidates[previous]:
                for i in range(len(word)):
                    part1=word[:i]; part2=word[i+1:]
                    for j in 'abcdefghijklmnopqrstuvwxyz':
                        if word[i]!=j:
                            nextword=part1+j+part2
                            if nextword in dict:
                                prevMap[nextword].append(word)
                                candidates[current] |= {nextword}

            if len(candidates[current])==0: return []  

        self.buildpath(prevMap, end, [], result)
        return result

    def buildpath(self, prevMap, word, path, result):
        
        if len(prevMap[word])==0:
            path.append(word)
            result.append(path[::-1])
            path.pop()
            return

        path.append(word)
        for predecessor in prevMap[word]:
            self.buildpath(prevMap, predecessor, path, result)  
        path.pop()

        
        

if __name__=="_"_"m"a"i"n"_"_"":""
"" "" "" "" ""p""r""i""n""t"" ""S""o""l""u""t""i""o""n""("")"".""f""i""n""d""L""a""d""d""e""r""s""(