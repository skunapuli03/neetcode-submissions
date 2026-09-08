class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        last_seen = set()

        for num in nums:
            if num in last_seen:
                return num
            else:
                last_seen.add(num)  
              
        
