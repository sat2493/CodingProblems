''' Did not pass all test cases '''

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        init_target = target
        index1 = -1
        index2 = -1
        
        while target >= 0:
            for num, index in zip(nums, range(len(nums))):
                if num == init_target - target:
                    index1 = index
                if num == target:
                    index2 = index
                 
            target = target - 1
        
        return [min([index1, index2]), max([index1, index2])]
