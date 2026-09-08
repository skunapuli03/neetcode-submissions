class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #a empty set 
        # see if each index has the same element, so for iteration of the nums array
        # we check to see if there is both in set and nums if so, return true
        # else it is false

        numSet = set()
        for n in nums:
            if n in numSet:
                return True
            else:
                numSet.add(n)
        return False