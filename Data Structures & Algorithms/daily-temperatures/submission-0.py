class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        results = [0]*len(temperatures)
        stack = []
        for i in range(0,len(temperatures)):
            if len(stack) == 0 or temperatures[i] < stack[-1][0]:
                stack.append((temperatures[i],i))
            else:
                while len(stack) > 0 and temperatures[i] > stack[-1][0]:
                    temp = stack.pop()
                    results[temp[1]] = i - temp[1]
                stack.append((temperatures[i],i))
        
        return results