class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        cter1 = 1;
        cter2 = 1;
        best = 1;
        for i in range(len(nums)-1):
            if nums[i+1] > nums[i]:
                cter2 +=1
                cter1 =1
            elif nums[i] > nums[i+1]:
                cter1 +=1
                cter2 = 1
            else:
                cter1,cter2 =1, 1
                
            best= max(best, cter1,cter2)
        return best