
__author__ = 'Danyang'
class Solution:
    def findSubstring_TLE(self, S, L):
        
        if not L:
            return

        k = len(L[0])
        l = len(L)

        working_list = list(L)
        result = []
        window_t = -1  
        window = []
        i = 0
        while i<=len(S)-3:
            
            if len(window)==l:
                result.append(window_t-l*k)

            word = S[i:i+3]
            if word in working_list:
                window.append(word)
                working_list.remove(word)
                window_t = i+3
                i += 3

            elif word not in L:
                if window:
                    i = window_t-len(window)*k+1  
                else:
                    i += 1

                window = []
                window_t = -1
                working_list = list(L)


            elif word in L and word not in working_list:
                window = window[window.index(word)+1:]
                window.append(word)
                
                window_t = i+3
                i += 3

        return result

    def findSubstring(self, S, L):
        
        if not L:
            return

        k = len(L[0])
        l = len(L)

        Lmap = {}  
        for item in L:
            if item in Lmap:
                Lmap[item] += 1
            else:
                Lmap[item] = 1

        Lmap_original = dict(Lmap)

        ret = []
        win_e = -1  
        working_win = []
        i = 0
        while i<len(S):
            
            if len(working_win)==l:
                ret.append(win_e-l*k)
                candidate = win_e-l*k+1
                if S[candidate:candidate+k] in Lmap:
                    win_e = -1
                    i = candidate
                    Lmap = dict(Lmap_original)
                    working_win = []

            word = S[i:i+k]
            
            if word in Lmap and Lmap[word]>0:
                working_win.append(word)
                Lmap[word] -= 1
                win_e = i+k
                i += k

            
            elif word not in Lmap:
                if working_win:
                    i = win_e-len(working_win)*k+1  
                else:
                    i += 1

                working_win = []
                win_e = -1
                Lmap = dict(Lmap_original)

            
            elif word in Lmap and Lmap[word]==0:
                for j in xrange(0, working_win.index(word)+1):  
                    Lmap[working_win[j]] += 1  
                working_win = working_win[working_win.index(word)+1:]
                working_win.append(word)
                Lmap[word] -= 1
                win_e = i+k
                i += k

        if len(working_win)==l:  
            ret.append(win_e-l*k)

        return ret

if __name__=="_"_"m"a"i"n"_"_"":""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""f""i""n""d""S""u""b""s""t""r""i""n""g""(