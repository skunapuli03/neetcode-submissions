class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            diff = target - num

            if diff in seen:
                return [seen[diff], i]
            seen[num] = i
            #fuck idk where to go from here
            # so we got the diff at each index, but how do we output the index of the diff??
            #i wanna say another loop??? 
            #or is it num[j] = diff
             