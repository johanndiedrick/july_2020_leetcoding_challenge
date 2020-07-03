# https://medium.com/100-days-of-leetcode/day-18-prison-cells-after-n-days-6982179f0df9
    
class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        
        if N > 14:
            N = (N % 14) + 14
        else:
            N = N % 14
            
        previous_cells = [x for x in cells]
        current_cells = [x for x in cells]
        for j in range(N):
            if previous_cells[0] == 1: current_cells[0] = 0
            for i in range(1, len(cells) - 1):
                if (previous_cells[i-1] == 0 and previous_cells[i+1] == 0) or (previous_cells[i-1] == 1 and previous_cells[i+1] == 1):
                    current_cells[i] = 1
                else:
                    current_cells[i] = 0
            if previous_cells[7] == 1: current_cells[7] = 0            
            previous_cells = [x for x in current_cells]
        return current_cells
