class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_map = {}   # stores last seen index of each char
        start_ptr = 0   # start of current window
        mlength = 0     # max length so far

        for end_ptr in range(len(s)):
            curr_char = s[end_ptr]

            # shrink window if duplicate inside current window
            if curr_char in char_map and char_map[curr_char] >= start_ptr:
                start_ptr = char_map[curr_char] + 1

            # update last seen index
            char_map[curr_char] = end_ptr

            # calculate window length
            curr_length = end_ptr - start_ptr + 1
            mlength = max(mlength, curr_length)

        return mlength
