class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        
        list3 = []
        for i in range(len(list1) + len(list2)):
            list3.append([])
        
        index1 = 1
        for a in list1:
            index2 = 1
            for b in list2:
                if a == b:
                    list3[index1+index2-1].append(a)
                index2 = index2 + 1
            index1 = index1 + 1
                                        
        for i in list3:
            if i != []:
                return i
        
        return answer
