class Solution:
    def reverseBits(self, n: int) -> int:
        # result = 0
        # for _ in range(32):
        #     bit = n & 1            
        #     result = (result << 1) | bit 
        #     n >>= 1               
        # return result
        result = 0
        for i in range(32):
            remainder = n % 2
            result = result * 2 + remainder
            n = n // 2
        return result