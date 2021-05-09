
__author__ = 'Danyang'
class Solution:
    def minDistance(self, word1, word2):
        
        m = len(word1)
        n = len(word2)
        d = [[-1 for _ in xrange(n+1)] for _ in xrange(m+1)]


        for i in xrange(m+1):
            d[i][0] = i
        for j in xrange(n+1):
            d[0][j] = j


        for i in xrange(1, m+1):
            for j in xrange(1, n+1):
                if word1[i-1]==word2[j-1]:
                    d[i][j] = d[i-1][j-1]
                else:
                    d[i][j]= min(
                        d[i-1][j]+1,  
                        d[i][j-1]+1,  
                        d[i-1][j-1]+1  
                    )

        return d[-1][-1]


