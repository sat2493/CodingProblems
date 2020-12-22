class Solution:
    def solve(self, s):
        letter_set = set()
        for l in s:
            # new character
            if l not in letter_set:
                letter_set.add(l)
            else:
                return False
        
        return True
