class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        return (len(nums)*(len(nums)-1)>>1)-sum(map(comb,Counter(map(sub,range(len(nums)),nums)).values(),cycle([2])))