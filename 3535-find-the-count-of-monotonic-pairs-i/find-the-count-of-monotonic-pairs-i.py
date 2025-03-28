from math import comb
class Solution:
    def countOfPairs(self, nums: List[int]) -> int:
        # MOD = 10**9 + 7
        # a, b = 0, nums[0]
        # arr1 = [a]
        # arr2 = [b]
        # for i in nums[1:]:
        #     # min a possible
        #     a = max(a, i - b)
        #     b = i - a
        #     arr1.append(a)
        #     arr2.append(b)
        # # probablity question
        # # bars and stars
        # # we have to convert 5, 5, 5, 5 to 0, 0, 0, 0 in the end
        # # xi can be {0, 1, 2, 3, 4, 5}
        # # to find the number of times xi appears is the problem
        # # x0 + x1 + x2 + x3 + x4 + x5 = 4
        
        # # number of bars = 5
        # # number of stars = 4
        # # 9 choose 4 
        # arr_2_min = min(arr2)
        # if arr_2_min < 0:
        #     return 0
        # res = comb(arr_2_min + len(arr2), len(arr2))
        
        # return res % MOD

        # n, mn = len(nums), nums.pop(0)
        # num1, num2 = 0, mn
    
        # for num in nums:
        #     if num < num1: return 0

        #     if num > num1 + num2: 
        #         num1 = num - num2  

        #     num2 = num - num1

        #     if num2 < mn: mn = num2
        # return comb(n + mn, mn) % 1_000_000_007

        mi, mx = 0, nums[0]
        for num in nums:
            if num - mi < 0:
                return 0
            
            if num >= mi + mx:
                mi = num - mx # Really just = mi + num - (mi + mx)
            
            mx = num - mi
        """
        Every digit within either array can vary from its max to min by a maximum of (mx + 1).
        E.g. for decreasing array, the last digit can be [0, mx], length = mx + 1
        Therefore, every pair is just each of the (mx+1) increments taking place at different
        positions within the array. Equivalent ways to split array into (mx+1) == putting len(nums) into (mx+1) buckets.
        (len(nums) + (mx+1) - 1) choose len(nums)
        """
        return math.comb(len(nums)+mx, mx) % (10**9 + 7)