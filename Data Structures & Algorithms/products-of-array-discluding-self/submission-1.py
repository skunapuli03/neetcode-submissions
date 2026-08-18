class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # I need the product of everything except the number at each index.
        # Since I cannot divide, I will get:
        # product of numbers to the left * product of numbers to the right.

        # This is where the final answers will go.
        # Start with 1 because multiplying by 1 does not change anything.
        res = [1] * len(nums)

        # prefix keeps track of the product of everything I have passed
        # from the left side so far.
        prefix = 1

        # First pass: put the left-side product into every answer spot.
        for i in range(len(nums)):

            # At this point, prefix is the product of everything LEFT of i.
            res[i] = prefix

            # Now include nums[i] so it is part of the left product
            # for the next index.
            prefix *= nums[i]

        # suffix keeps track of the product of everything to the right.
        suffix = 1

        # Second pass: go backward so suffix represents everything RIGHT of i.
        for i in range(len(nums) - 1, -1, -1):

            # res[i] already has the left product.
            # Multiply by the right product to get the full answer.
            res[i] *= suffix

            # Now include nums[i] so it is part of the right product
            # for the next index to the left.
            suffix *= nums[i]

        return res