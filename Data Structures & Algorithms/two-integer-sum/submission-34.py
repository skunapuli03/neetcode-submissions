class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #need to return indexes of the values that add up to a target num
        #need difference as target given, and we can get the value based on a for loop index
        #use enumerate so we can store in map if need be or turn thelist into a map
        output = {}

        for i, num in enumerate(nums):
            diff = target - num #for every number, we find the difference at every i, so it is diff: i
            if diff in output:
                return [output[diff], i]

            output[num] = i #if lets say the value doesnt exist