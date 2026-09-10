class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        nums.sort()

        big1 = nums[-1]
        big2 = nums[-2]

        smol1 = nums[0]
        smol2 = nums[1]

        return (big1*big2) - (smol1*smol2)