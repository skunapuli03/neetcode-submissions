class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #need a map to keep track of number: times of appearance
        #then return the numbers that >= k, as an array 
        freq = {}

        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        #to keep the track of each num, and its count u write it in a bucket like approach where it is bucket[count]
        buckets = [[] for _ in range(len(nums) + 1)]

        for num, count in freq.items():
            buckets[count].append(num)

        res = []

        for count in range(len(buckets) -1, 0, -1):
            for num in buckets[count]:
                res.append(num)

                if len(res) == k:
                    return res        


