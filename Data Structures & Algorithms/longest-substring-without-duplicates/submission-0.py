class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        characters = set()
        p1 = 0
        max_length = 0
        for p2 in range(len(s)):
            while s[p2] in characters:
                characters.remove(s[p1])
                p1+=1
            characters.add(s[p2])
            max_length = max(max_length,p2-p1+1)
        return max_length