class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        for _ in range(k):
            min_index = 0
            for i in range(len(nums)):
                if nums[i] < nums[min_index]:
                    min_index = i
            nums[min_index] *= multiplier
        return nums

        