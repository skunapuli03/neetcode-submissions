class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        ptr1 = 0

        while ptr1 <= len(haystack) - len(needle):
            ptr2 = 0

            while ptr2 < len(needle) and haystack[ptr1+ptr2] == needle[ptr2]:
                ptr2+=1

            if ptr2 == len(needle):
                return ptr1
            
            ptr1+=1
        
        return -1 