# Runtime: 44 ms, faster than 75.60% of Python3 online submissions for Valid Anagram.
# Memory Usage: 14.4 MB, less than 76.20% of Python3 online submissions for Valid Anagram.


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_hashmap = {}
        t_hashmap = {}
        
        # Case different sizes
        if len(s) != len(t):
            return False
        
        # Store in hash maps.
        for letter in s:
            # Add letter into hashmap
            # If letter exists, increase frequency by 1
            try:
                s_hashmap[letter] = s_hashmap[letter] + 1
                
            # If letter not exists, create a new entry with frequency 1
            except:
                s_hashmap[letter] = 1
            
        for letter in t:
            # Add letter into hashmap
            # If letter exists, increase frequency by 1
            try:
                t_hashmap[letter] = t_hashmap[letter] + 1
                
            # If letter not exists, create a new entry with frequency 1
            except:
                t_hashmap[letter] = 1
            
        # Compare hash maps.
        try:
            # Assume that s and t both share the same letters
            for letter in s:
                if s_hashmap[letter] != t_hashmap[letter]:
                    return False
            return True
        
        except:
            return False 
