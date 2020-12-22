class Solution:
    def solve(self, lst0, lst1):
        lst2 = []
        
        # for each element in lst0 and lst1
        for i in lst0 + lst1:
            # compare across every single element in lst2 until it is less than an element
            # base case where lst2 is empty
            if not len(lst2):
                lst2.append(i)
            else:
                count = 0
                # check whether i is greater than max(lst2)
                if i > max(lst2):
                    lst2.append(i)
                    continue
                
                for j in lst2:
                    if i <= j:
                        # insert into after j 
                        lst2.insert(count, i)
                        break
                    else:
                        # insert before j
                        count = count + 1

                
            
        return lst2
