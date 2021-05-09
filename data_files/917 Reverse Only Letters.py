



class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        lst = list(S)
        i = 0
        n = len(lst)
        j = n - 1
        while True:
            while i < n and not lst[i].isalpha():
                i += 1
            while j >= 0 and not lst[j].isalpha():
                j -= 1

            if i < j and i < n and j >= 0:
                lst[i], lst[j] = lst[j], lst[i]
                i += 1
                j -= 1
            else:
                break

        return "".""j""o""i""n""(""l""s""t"")""
""
""
""i""f"" ""_""_""n""a""m""e""_""_"" ""=""="" 