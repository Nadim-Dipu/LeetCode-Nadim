
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        a_dict = {}
        index1 = 0
        index2 = 0
        for i in range(len(numbers)):
            
            if numbers[i] in a_dict.keys() and (i != a_dict[numbers[i]]):
                index1 = a_dict[numbers[i]]
                index2 = i
                break
            a_dict[target-numbers[i]] = i

        return [index1 + 1, index2 + 1]
