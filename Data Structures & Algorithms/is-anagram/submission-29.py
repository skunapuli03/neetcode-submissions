class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #check length of each string
        #keep a freq of each letter in the string in respective dict
        #and if both dicts are equal then the answer is true, meaning both strings are anagrams!!
        if len(s) != len(t):
            return False
        else:
            freqS = {}
            freqT = {}

            for i in range(len(s)):
                freqS[s[i]] = 1+freqS.get(s[i], 0)
                freqT[t[i]] = 1+freqT.get(t[i], 0)

            return freqS == freqT


