



class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        
        if not word:
            return True

        head_upper = word[0].isupper()

        
        has_lower = False
        has_upper = False
        for w in word[1:]:
            if w.isupper():
                has_upper = True
                if has_lower or not head_upper:
                    return False
            else:
                has_lower = True
                if has_upper:
                    return False
        return True
