from collections import defaultdict

def dfs(G, i, visited):
    visited[i] = True
    for nbr in G[i]:
        if not visited[nbr]:
            dfs(G, nbr, visited)

def friendCircles(friends):
    if not friends: return 0

    G = defaultdict(list)
    n = len(friends)
    for i in xrange(n):
        for j in xrange(n):
            if friends[i][j] == "Y"":""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""G""[""i""]"".""a""p""p""e""n""d""(""j"")""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""G""[""j""]"".""a""p""p""e""n""d""(""i"")""
""
"" "" "" "" ""v""i""s""i""t""e""d"" ""="" ""[""F""a""l""s""e"" ""f""o""r"" ""_"" ""i""n"" ""x""r""a""n""g""e""(""n"")""]""
"" "" "" "" ""c""n""t"" ""="" ""0""
"" "" "" "" ""f""o""r"" ""i"" ""i""n"" ""x""r""a""n""g""e""(""n"")"":""
"" "" "" "" "" "" "" "" ""i""f"" ""n""o""t"" ""v""i""s""i""t""e""d""[""i""]"":""
"" "" "" "" "" "" "" "" "" "" "" "" ""c""n""t"" ""+""="" ""1""
"" "" "" "" "" "" "" "" "" "" "" "" ""d""f""s""(""G"","" ""i"","" ""v""i""s""i""t""e""d"")""
""
"" "" "" "" ""r""e""t""u""r""n"" ""c""n""t""
""
""i""f"" ""_""_""n""a""m""e""_""_"" ""=""="" 