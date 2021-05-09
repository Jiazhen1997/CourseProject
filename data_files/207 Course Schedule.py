
__author__ = 'Daniel'


class Solution:
    def canFinish(self, numCourses, prerequisites):
        
        V = [[] for _ in xrange(numCourses)]
        for edge in prerequisites:
            V[edge[0]].append(edge[1])

        visited = [False for _ in xrange(numCourses)]  
        marked = [False for _ in xrange(numCourses)]  
        for i in xrange(numCourses):
            if not visited[i]:
                if self.dfs_have_cycle(V, i, visited, marked):
                    return False

        return True

    def dfs_have_cycle(self, V, i, visited, marked):
        if marked[i]:
            return True

        marked[i] = True

        for neighbor in V[i]:
            if not visited[neighbor] and self.dfs_have_cycle(V, neighbor, visited, marked):
                return True

        
        marked[i] = False
        visited[i] = True
        return False


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""c""a""n""F""i""n""i""s""h""(""2"","" ""[""[""1"","" ""0""]"","" ""[""0"","" ""1""]""]"")"" ""i""s"" ""F""a""l""s""e