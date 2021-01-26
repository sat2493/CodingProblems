# UNTESTED

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        symbols = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
        values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        
        integer = 0
        
        for symbol, value in zip(symbols, values):
            while s[0 : len(symbol) + 1] == symbol:
                integer = integer + value
                s = s[len(symbol) : len(s)]
                
        return integer
