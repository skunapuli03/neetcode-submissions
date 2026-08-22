class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #need a map to keep track of number: times of appearance
        #then return the numbers that >= k, as an array 
        freq = {}

        for num in nums:
            freq[num] = freq.get(num, 0) + 1
# Now I need to organize numbers by their counts.
        # buckets[count] will contain all numbers that appeared `count` times.
        buckets = [[] for _ in range(len(nums) + 1)]

        # Flip the relationship:
        # from number -> count
        # into count -> list of numbers.
        for num, count in freq.items():
            buckets[count].append(num)

        # I need exactly k numbers, starting with the highest frequencies.
        res = []

        # Start at the largest possible count and move downward.
        for count in range(len(buckets) - 1, 0, -1):
            for num in buckets[count]:
                res.append(num)

                # Once I have k numbers, they must be the k most frequent.
                if len(res) == k:
                    return res

