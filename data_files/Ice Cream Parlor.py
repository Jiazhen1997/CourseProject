

__author__ = 'Danyang'


class Solution(object):
    def solve(self, cipher):
        
        M, N, C = cipher
        hash_map = {}
        for ind, val in enumerate(C):
            if val in hash_map:
                hash_map[val].append(ind)
            else:
                hash_map[val] = [ind]
        for ind, val in enumerate(C):
            target = M - val
            if target in hash_map:
                i = 0
                while i < len(hash_map[target]) and hash_map[target][i] <= ind:
                    i += 1
                if i != len(hash_map[target]):
                    return "%"d" "%"d"" ""%"" ""(""i""n""d"" ""+"" ""1"","" ""h""a""s""h""_""m""a""p""[""t""a""r""g""e""t""]""[""i""]"" ""+"" ""1"")""
""
""
""i""f"" ""_""_""n""a""m""e""_""_"" ""=""="" 