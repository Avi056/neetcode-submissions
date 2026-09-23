class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        toRet = []
        
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            p1 = i + 1
            p2 = len(nums) - 1
            target = -nums[i] 
            
            while p1 < p2:
                current_sum = nums[p1] + nums[p2]
                
                if current_sum == target:
                    toRet.append([nums[i], nums[p1], nums[p2]])
                    
                    while p1 < p2 and nums[p1] == nums[p1 + 1]:
                        p1 += 1
                    while p1 < p2 and nums[p2] == nums[p2 - 1]:
                        p2 -= 1
                        
                    p1 += 1
                    p2 -= 1
                elif current_sum > target:
                    p2 -= 1
                else:
                    p1 += 1
                    
        return toRet