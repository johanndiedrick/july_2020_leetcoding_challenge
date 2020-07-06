class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        distance = 0
        
        xor = x ^ y
        
        while xor > 0:
            distance += xor & 1
            xor >>= 1
            
        return distance
