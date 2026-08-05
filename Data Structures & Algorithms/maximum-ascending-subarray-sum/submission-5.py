class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        #similar to a problem
        #the goal is to keep track of what 
        reset = nums[0]
        curr_sum = nums[0]
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                reset += nums[i]
            else:
                curr_sum = max(curr_sum, reset)
                reset = nums[i]

        return max(curr_sum, reset)            