class Solution:
    def sortColors(self, nums: List[int]) -> None:
        # zero = 0
        # two = len(nums) - 1
        # curr = 0

        # while curr <= two:
        #     if nums[curr] == 0:
        #         nums[curr], nums[zero] = nums[zero], nums[curr]
        #         zero += 1
        #         if curr < zero :
        #             curr = zero
        #     elif nums[curr] == 2:
        #         nums[curr], nums[two] = nums[two], nums[curr]
        #         two -= 1
        #     else:
        #         curr += 1


        zero = one = 0
        for two in range(len(nums)):
            tmp = nums[two]
            nums[two] = 2
            if tmp < 2:
                nums[one] = 1
                one += 1
            if tmp < 1:
                nums[zero] = 0
                zero += 1


        