
class Solution:
    def hammingWeight(self, n: int) -> int:
        str1 = '{:032b}'.format(n)
        return str1.count("1")
        
