
class Solution:
    def reverseBits(self, n: int) -> int:
        str1 = '{:032b}'.format(n)
        str2 = str1[::-1]
        return int(str2,2)
