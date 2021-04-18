# Incomplete

import math

class Solution:
    def isHappy(self, n: int) -> bool:
        
        
        while n != 1:
            n_temp = n
            # Extract digits:
            while n_temp != 0:
                
                # Update n_temp
                n_temp = math.floor(n_temp / 10)
            
            # Case return to n
            
            # Update n
        return True
