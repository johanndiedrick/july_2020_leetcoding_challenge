class Solution:
    def arrangeCoins(self, n: int) -> int:
        if n == 1:
            return 1
        total_rows = 0
        for val in range(1, n + 1):
            n -= val
            if n < 0:
                break
            else:
                total_rows += 1
        return total_rows
