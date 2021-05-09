

from typing import List


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        
        ret = []
        char_cnt = 0  
        cur_words = []

        for w in words:
            cur_words.append(w)
            char_cnt += len(w)
            if char_cnt + len(cur_words) - 1 > maxWidth:
                
                cur_words.pop()
                char_cnt -= len(w)
                for i in range(maxWidth - char_cnt):
                    cur_words[i % max(1, len(cur_words) - 1)] += " ""
""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""r""e""t"".""a""p""p""e""n""d""(
        Round robin distribution of spaces

        Look before jump
        Look before you leap
        