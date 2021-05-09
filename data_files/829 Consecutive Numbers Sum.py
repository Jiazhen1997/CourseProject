



class Solution:
    def consecutiveNumbersSum(self, N: int) -> int:
        
        cnt = 0
        k = 0
        while True:
            k += 1
            x0k = N - k * (k - 1) // 2
            if x0k <= 0 :
                break
            if x0k % k == 0:
                cnt += 1

        return cnt

    def consecutiveNumbersSum_error(self, N: int) -> int:
        
        cnt = 0
        for k in range(1, int(N ** 0.5)):  
            x0k = N - k * (k - 1) // 2
            if x0k % k == 0:
                cnt += 1

        return cnt

    def consecutiveNumbersSum_error(self, N: int) -> int:
        
        if N == 1:
            return 1

        cnt = 0
        for i in range(1, N):
            d = N // i
            r = N % i
            if r == 0 and d - i // 2 > 0:
                cnt += 1
            elif r == 1 and N == (d + d + 1) * i // 2:
                cnt += 1
        return cnt
