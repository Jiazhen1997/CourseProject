
__author__ = 'Danyang'


class Solution:
    def maxDiffSubArrays(self, nums):
        
        n = len(nums)
        min_left = list(nums)
        max_left = list(nums)
        min_right = list(nums)
        max_right = list(nums)


        
        current = 0
        for i in xrange(n):
            current += nums[i]
            if i-1 >= 0:
                min_left[i] = min(current, min_left[i-1], min_left[i])
            else:
                min_left[i] = min(current, min_left[i])

            if current > 0:
                current = 0

        
        current = 0
        for i in xrange(n):
            current += nums[i]
            if i-1 >= 0:
                max_left[i] = max(current, max_left[i-1], max_left[i])
            else:
                max_left[i] = max(current, max_left[i])

            if current < 0:
                current = 0

        current = 0
        for i in xrange(n-1, -1, -1):
            current += nums[i]
            if i+1 <= n-1:
                max_right[i] = max(current, max_right[i+1], max_right[i])
            else:
                max_right[i] = max(current, max_right[i])

            if current < 0:
                current = 0

        current = 0
        for i in xrange(n-1, -1, -1):
            current += nums[i]
            if i+1 <= n-1:
                min_right[i] = min(current, min_right[i+1], min_right[i])
            else:
                min_right[i] = min(current, min_right[i])

            if current > 0:
                current = 0

        maxa = 0
        for i in xrange(n-1):
            maxa = max(maxa, abs(max_left[i]-min_right[i+1]), abs(min_left[i]-max_right[i+1]))

        return maxa


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""p""r""i""n""t"" ""S""o""l""u""t""i""o""n""("")"".""m""a""x""D""i""f""f""S""u""b""A""r""r""a""y""s""(""[""-""4"","" ""5"","" ""-""4"","" ""5"","" ""-""4"","" ""5"","" ""-""4"","" ""5"","" ""-""4"","" ""5"","" ""-""4"","" ""5"","" ""-""4"","" ""5"","" ""-""4"","" ""5"","" ""-""4"","" ""5"","" ""-""1""0""0""0""]"")""
""
""
""
