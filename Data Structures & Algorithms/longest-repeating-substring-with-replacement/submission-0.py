class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        curr_max = 0
        best_max = 0
        p1=0
        count = {}
        for p2 in range(len(s)):
            count[s[p2]] = 1 + count.get(s[p2],0)
            curr_max = max(curr_max,count[s[p2]])
            while (p2-p1+1) - max(count.values()) > k:
                count[s[p1]] -= 1
                p1 += 1
            best_max = max(best_max,p2-p1+1)
        return best_max