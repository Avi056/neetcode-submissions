class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        max_sequence = 0
        for i in range(len(nums)):
            if nums[i]-1 not in nums_set:
                curr = nums[i]
                curr_sequence = 0
                while curr in nums_set:
                    curr_sequence += 1
                    curr +=1
                if curr_sequence > max_sequence:
                    max_sequence = curr_sequence

        return max_sequence