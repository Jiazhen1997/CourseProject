
__author__ = 'Danyang'


class Solution:
    def lengthOfLongestSubstring(self, s):
        
        
        visited_last_index = [-1 for _ in range(256)]  
        longest = 0  

        start = 0  
        for ind, val in enumerate(s):
            if visited_last_index[ord(val)] == -1:
                longest = max(longest, (ind)-start+1)
            else:
                longest = max(longest, (ind-1)-start+1)

                
                for i in range(start, visited_last_index[ord(val)]):
                    visited_last_index[ord(s[i])] = -1

                start = visited_last_index[ord(val)]+1

            visited_last_index[ord(val)] = ind  

        return longest