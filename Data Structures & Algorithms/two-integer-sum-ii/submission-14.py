class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1 #you do -1 bc arrays indexing starts at 0, and to prevent us from pointer being out of range
        while l < r:
            total = numbers[l] + numbers[r]

            if total == target:
                return [l + 1, r + 1] #we do + 1 here because the problem asks for 1 index, but we solve the problem or the core algo as if we are dealing with regular index
            elif total < target:
                l += 1
            else:
                r -= 1