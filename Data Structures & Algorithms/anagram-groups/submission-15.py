class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for word in strs:
            count = [0]*26
            for c in word:
                count[ord(c) - ord("a")] +=1

            key = tuple(count)
            
            if key not in groups:
                groups[key] = []
            groups[key].append(word)

        return list(groups.values())                

#my intuition:
#For each word:

#1. Count the frequency of each letter.
#2. That frequency becomes the "key."
#3. Use a dictionary:
 #     key -> list of words
#4. If the key already exists,
   ##   append the word.
#5. Otherwise,
  #    create a new list.
#6. At the end,
      #return all of the dictionary's values.

