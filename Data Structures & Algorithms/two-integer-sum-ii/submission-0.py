class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #target - index1 = index2
        #index1 < index2
        #for i in numbers:
        #   target - index1 = index2
        #   if index1< index 2:
        #       return [numbers[index1], numbers[index2]]

        l = 0
        r = len(numbers) - 1

        while l<r:
            curSum = numbers[l] + numbers[r]
            if curSum > target:
                r-= 1
            elif curSum < target:
                l+=1
            elif curSum == target:
                return [l+1, r+1]
        return []
