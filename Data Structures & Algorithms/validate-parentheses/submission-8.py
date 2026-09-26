class Solution:
    def isValid(self, s: str) -> bool:
        # 1 & 2. Create stack and map
        stack = []
        bracket_map = {")": "(", "]": "[", "}": "{"}
        
        # 3. Loop through every character
        for char in s:
            # 4. If it's an OPENING bracket (it's not a key in our map)
            if char not in bracket_map:
                stack.append(char)
                
            # 5. If it's a CLOSING bracket (it is a key in our map)
            else:
                # If stack is empty, we can't pop anything
                if not stack:
                    return False
                
                top_bracket = stack.pop()
                
                # Check if it matches the correct pair in the map
                if bracket_map[char] != top_bracket:
                    return False
                    
        # 6. If the stack is empty at the end, it returns True.
        return not stack 
