class Solution:
    def minNonZeroProduct(self, p: int) -> int:
        if p == 1:
            return 1
        return (pow(2**p -2, 2**(p-1) - 1, 10**9 + 7) * (2**p - 1)) % (10**9 + 7)
        max_num = pow(2,p)-1
        power = max_num//2

        return (pow(max_num-1, power, 10**9 + 7) * (max_num)) % (10**9 + 7)