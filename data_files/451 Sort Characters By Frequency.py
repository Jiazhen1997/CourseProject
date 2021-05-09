

from collections import defaultdict


class Solution(object):
    def frequencySort(self, s):
        
        counter = defaultdict(int)
        for c in s:
            counter[c] += 1

        bucket = {count: [] for count in range(1, len(s)+1)}
        for k, v in counter.items():
            bucket[v].append(k)

        ret = []
        for count in reversed(range(1, len(s) + 1)):
            if bucket[count]:
                for c in bucket[count]:
                    ret.append(c * count)

        return "".""j""o""i""n""(""r""e""t"")""
""
""
""i""f"" ""_""_""n""a""m""e""_""_"" ""=""="" 