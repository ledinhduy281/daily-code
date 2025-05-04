class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        digits = [len(str(num)) for num in nums]
        for digit in digits:
            if digit % 2 == 0:
                count += 1
        return count
        