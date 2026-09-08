class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #hashmap implementation
        #check if strs r the same length
        #then check to see if they have same chars
        #if yes, print them 
        anagrams = {}
        anagram_list =[]
        for i in strs:
            count = [0] *26
            for char in i:
                count[ord(char)-ord('a')]+=1
            key = tuple(count)

            if key not in anagrams:
                anagrams[key] = []
            anagrams[key].append(i)
            
        return list(anagrams.values())