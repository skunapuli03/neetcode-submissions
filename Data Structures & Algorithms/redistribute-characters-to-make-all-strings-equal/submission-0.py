class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        #u check the next element to see if it has repeated aka store a count of how common each character is
        #make sure that chars are split evenly across every word. 

        ct = {}
        for word in words:
            for c in word:
                ct[c] = ct.get(c, 0)+1

        for c in ct:
            if ct[c] % len(words) != 0:
                return False

        return True