class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # A set gives me fast O(1)-average checks:
        # "Does this number exist?"
        num_set = set(nums)

        # This will hold the longest sequence length I find.
        longest = 0

        # Look at every unique number.
        for num in num_set:

            # I only care if num is the START of a sequence.
            # If num - 1 exists, then some earlier number will already
            # count this sequence, so I skip it.
            if num - 1 not in num_set:

                # num starts a new sequence, so it has length 1 so far.
                length = 1

                # Keep checking for the next number in the sequence.
                while num + length in num_set:
                    length += 1

                # Keep whichever sequence is longer.
                longest = max(longest, length)

        return longest