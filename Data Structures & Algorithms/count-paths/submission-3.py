class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        old_row = [1] * n
        for i in range(m-1,0,-1):
            curr_row = [1] * n
            for j in range(n-1-1,-1,-1):
                curr_row[j] = curr_row[j+1] + old_row[j]
            old_row = curr_row

        return old_row[0]
