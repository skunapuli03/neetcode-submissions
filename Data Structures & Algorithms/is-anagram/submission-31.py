class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #two strings given
        #check if they same length
        #check the frequency of each letter?

        #counter, a frequency problem, so need a dict/map
        #but before that check the lengths
        if len(s) != len(t):
            return False
        
        freq = [0] * 26

        #so what we now check for each freq is wehther the same amount of chars appear in s also appear in t, we do that by 
        
        for c in range(len(s)):
            freq[ord(s[c])-ord("a")] += 1
            freq[ord(t[c])-ord("a")] -= 1
            
        for ch in freq:
            if ch != 0:
                return False
        return True

        