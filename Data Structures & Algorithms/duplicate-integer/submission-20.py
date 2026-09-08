class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numSet = set()
        res = False
        for i in nums:
            if i in numSet:
                res = True
            else: 
                numSet.add(i)

        return res
    
