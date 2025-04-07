class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        sum_nums = sum(nums)

        if sum_nums % 2 != 0:
            return False

        half_sum_nums = sum(nums) // 2
        sum_element = 0

        # for i in range(len(nums)):
        #     sum_element = nums[i]
        #     for j in range(i+1, len(nums)):
        #         sum_element += nums[j]
        #         if sum_element == half_sum_nums:
        #             return True
        #         elif sum_element > half_sum_nums:
        #             break
        # return False
        dp = [False] * (half_sum_nums + 1)
        dp[0] = True
        for num in nums:
            for current_sum in range(half_sum_nums, num - 1, -1):
                dp[current_sum] = dp[current_sum] or dp[current_sum - num]
        return dp[half_sum_nums]