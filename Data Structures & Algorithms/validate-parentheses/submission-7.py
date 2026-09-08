class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpenBracMap = { ")" : "(", "]" : "[", "}" :"{" }

        for c in s:
            if c in closeToOpenBracMap:
                if stack and stack[-1] == closeToOpenBracMap[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        return True if not stack else False