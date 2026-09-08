class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Dictionary to store the last seen index of each character
        # Key: character, Value: index
        char_index_map = {}
        
        # Pointers for the sliding window
        start_ptr = 0
        
        # Variable to track the maximum length found so far
        max_length = 0
        
        # 'end_ptr' (i) iterates through the string, expanding the window
        for end_ptr in range(len(s)):
            current_char = s[end_ptr]
            
            # 1. Check for Duplicate Character:
            # If the current character is already in the map AND
            # its last seen index is greater than or equal to the start_ptr,
            # it means the duplicate is inside the current window.
            if current_char in char_index_map and char_index_map[current_char] >= start_ptr:
                
                # Shrink the window: Move the start_ptr past the last occurrence
                # of the duplicate character.
                start_ptr = char_index_map[current_char] + 1
            
            # 2. Update the Map:
            # Always update the character's index to its current position.
            char_index_map[current_char] = end_ptr
            
            # 3. Calculate and Update Max Length:
            # The current length is (end_ptr - start_ptr + 1).
            # We use max() to keep track of the overall longest valid window.
            current_length = end_ptr - start_ptr + 1
            max_length = max(max_length, current_length)
            
        return max_length