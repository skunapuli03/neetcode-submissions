class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #deal with two pointers, left to right? or sliding window type setup
        # the goal is to multiply the local maximum and the global max
        # so if we use pointers how are we going to set up the global and local max
        #trying to find an area so width or indexes from the global max matters

        l = 0
        r = len(heights) - 1
        gmax = 0
        while l < r:
            width = r - l
            area = min(heights[l], heights[r]) * width
            gmax = max(gmax, area)
            if heights[l] < heights[r]:
                l+=1
            else:
                r -=1
        return gmax


