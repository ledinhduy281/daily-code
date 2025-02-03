class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        inc = dec = max_length = 1
        for x, y in pairwise(nums):
            inc = inc + 1 if x < y else 1
            dec = dec + 1 if x > y else 1
            max_length = max(inc,dec,max_length)
        return max_length
        