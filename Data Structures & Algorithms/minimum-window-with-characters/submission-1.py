class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_counts = {}
        for char in t:
            t_counts[char] = t_counts.get(char, 0) + 1
            
        minl = 0 
        minr = 0 
        l = 0 
        curr_min = float('inf')
        chars = {i: 0 for i in t_counts} 
        found_any = False 

        for r in range(len(s)):
            if s[r] in chars:
                chars[s[r]] += 1
            
            valid = True
            for i in t_counts:
                if chars[i] < t_counts[i]:
                    valid = False
                    break
            
            looped = False
            while valid:
                looped = True
                if s[l] in chars:
                    chars[s[l]] -= 1
                l += 1
                
                for i in t_counts:
                    if chars[i] < t_counts[i]:
                        valid = False
                        break
            
            if looped:
                found_any = True
                l -= 1
                chars[s[l]] += 1
                if r - l + 1 < curr_min:
                    curr_min = r - l + 1 
                    minl = l 
                    minr = r
                    
        if not found_any: 
            return "" 
            
        return s[minl:minr+1]
