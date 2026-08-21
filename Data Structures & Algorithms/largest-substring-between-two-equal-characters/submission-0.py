class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        seen = {}
        maxcount = -1
        for i, c in enumerate(s):
            if c in seen:
                count = i - seen[c] - 1
                maxcount = max(maxcount, count)
            else:
                seen[c] = i

        return maxcount
            


