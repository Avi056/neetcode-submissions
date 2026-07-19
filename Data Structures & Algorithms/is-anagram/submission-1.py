class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        sDict = {}
        
        for i in s:
            sDict[i] = sDict.get(i,0)+1

        tDict = {}
        
        for i in t:
            tDict[i] = tDict.get(i,0)+1
        
        if sDict == tDict:
            return True
        else:
            return False
