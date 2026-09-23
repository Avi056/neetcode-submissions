class Solution:
    def trap(self, height: List[int]) -> int:
        prefix = [0]*len(height)
        suffix = [0]*len(height)
        curr_max = 0
        rcurr_max = 0

        total_water = 0

        for i in range(len(height)-1):
            prefix[i] = curr_max
            if height[i] > curr_max:
                curr_max = height[i]

            suf_i = len(height)-i-1
            suffix[suf_i] = rcurr_max
            if height[suf_i] > rcurr_max:
                rcurr_max = height[suf_i]

        for i in range(len(height)):
            total_water += max(0,min(prefix[i],suffix[i]) - height[i])

        return total_water
