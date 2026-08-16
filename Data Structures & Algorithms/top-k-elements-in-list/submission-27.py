class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # First, I need to know how often every number appears.
        # This will become: number -> its count.
        count = {}

        # A number can appear at most len(nums) times.
        # Each index represents a frequency.
        #
        # Example: freq[3] will hold every number that appeared 3 times.
        freq = [[] for _ in range(len(nums) + 1)]

        # Count each number.
        for n in nums:

            # If I have not seen n before, start its count at 0.
            # Then add 1 for this occurrence.
            count[n] = 1 + count.get(n, 0)

        # Now I know each number's frequency.
        # Put each number into the bucket for its frequency.
        for n, c in count.items():

            # Example: if 7 appeared 3 times,
            # put 7 into freq[3].
            freq[c].append(n)

        # I need to return the k MOST frequent numbers.
        res = []

        # Start at the highest possible frequency and move downward.
        # -1 means move backwards by one each time.
        for i in range(len(freq) - 1, 0, -1):

            # There may be multiple numbers with frequency i.
            for n in freq[i]:

                # This number is one of the most frequent remaining numbers.
                res.append(n)

                # Once I have k numbers, I am done.
                if len(res) == k:
                    return res