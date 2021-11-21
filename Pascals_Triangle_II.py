
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        pascal = []
        for i in range(rowIndex + 2):
            array = []
            for j in range(i):
                if i >= 2 and (j != 0 and j != i-1):
                    array.append(pascal[i-1][j-1] + pascal[i-1][j])
                else:
                    array.append(1)
    
            pascal.append(array)
    
        return pascal[rowIndex + 1]
