class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #keep a dict of how many times a letter shows up in the string
        #two pass approach where lets say we see a letter in string s, we set that s[i] = 1, and if that same s[i] = t[i] then we subtract 1 from the str s dict. so if all are equal to 0 or s[i] == t[i] then they are the anagram right
        #but before that we must do the following: CHECK THE LENGTHHH!!!
        
        freqS = {}
        freqT = {}
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            freqS[s[i]] = 1 + freqS.get(s[i], 0)
            freqT[t[i]] = 1 + freqT.get(t[i], 0)
        return freqS == freqT 
