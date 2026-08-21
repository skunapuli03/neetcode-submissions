class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()

        # set up pointers
        l = 0
        r = len(s) - 1 #minus one bc the indexing starts at 0

        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1
            if s[l] != s[r]:
                return False
            
            l += 1
            r -= 1
        return True