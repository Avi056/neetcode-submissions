class Solution:
    def isValid(self, s: str) -> bool:
        opposite = {'(':')','{':'}','[':']'}
        stack = []
        if len(s)%2 != 0:
            return False
        for i in range(len(s)):
            if s[i] in opposite.keys():
                stack.append(s[i])
            else:
                if len(stack) <= 0:
                    return False
                temp = stack.pop()
                if s[i] != opposite[temp]:
                    return False
        if len(stack) > 0:
            return False
        return True