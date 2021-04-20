# Incomplete

import math

class Solution:
    def isHappy(self, n: int) -> bool:
        
        digits = str(n)
        l = 0
        for digit in digits:
            l = l + int(digit) 
        
        while n != 1:
            # Extract digits:
            digits = str(n)
             
            # Update n
            n = 0
            for digit in digits:
                # Square the digits
                # Add each square to the sum
                n = n + (int(digit) * int(digit))
            print(n)
            
            # Adjust n
            digits = str(n)
            m = 0
            for digit in digits:
                m = m + int(digit)
            print("Adjusted: ", m)
            
            # Case return to n
            if m == l:
                return False
            
        return True
