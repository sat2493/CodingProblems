# 9:50
# Note: As of December 28, 2020, did not finish.

#def notAdjacent(array, i):
#    # check if left exists
#    if 

# def countOccupiedandAdjacentNeighbors(array):
#    m = 0
#    for i in range(len(array)):
#        # check left
#        if i != 0:
#            if array[i-1] 
#        if array[i] == 1:
#            m = m + 1
#    return m

class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        
        m = len(flowerbed)
        
        for i in range(len(flowerbed)):
            if flowerbed[i] == 1:
                m = m - 1
                continue
            if i != 0 and flowerbed[i-1] == 1:
                m = m - 1
                continue
            if i != len(flowerbed) - 1 and flowerbed[i+1] == 1:
                m = m - 1
                continue
                
        print(m)        
                
        if m >= n:
            return True
        else:
            return False
