class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # I need a place to collect groups of words.
        # The key will represent a word's letter frequencies.
        # The value will be the list of words with those frequencies.
        groups = {}

        # Look at one word at a time.
        for word in strs:

            # I need to count every letter in THIS word.
            # There are 26 lowercase letters, so make 26 counters.
            count = [0] * 26

            # Go through every character in the current word.
            for char in word:

                # Turn the letter into an index:
                # a -> 0, b -> 1, ..., z -> 25.
                letter_index = ord(char) - ord("a")

                # Add one to that letter's frequency.
                count[letter_index] += 1

            # Anagrams have the exact same frequency count.
            # A tuple can be a dictionary key; a list cannot.
            key = tuple(count)

            # If this is the first word with this letter count,
            # make an empty group for it.
            if key not in groups:
                groups[key] = []

            # Put the current word into its anagram group.
            groups[key].append(word)

        # I do not need the frequency keys anymore.
        # I only need the grouped lists of words.
        return list(groups.values())