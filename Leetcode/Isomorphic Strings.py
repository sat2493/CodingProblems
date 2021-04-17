# Runtime: 40 ms, faster than 69.00% of Python3 online submissions for Isomorphic Strings.
# Memory Usage: 14.9 MB, less than 12.87% of Python3 online submissions for Isomorphic Strings.

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        meta_s = []
        meta_t = []
        
        hashMap = {}
        
        count = 1
        for character in s:
            try:
                # character exists in hashMap
                # build the meta string
                meta_s.append(hashMap[character])
                
            except:
                # character does not exist in hashMap
                hashMap[character] = count
                count = count + 1
                
                # build the meta string
                meta_s.append(hashMap[character])
              
        hashMap = {}
        
        count = 1
        for character in t:
            try:
                # character exists in hashMap
                # build the meta string
                meta_t.append(hashMap[character])
                
            except:
                # character does not exist in hashMap
                hashMap[character] = count
                count = count + 1
                
                # build the meta string
                meta_t.append(hashMap[character])
                
        print(meta_s)
        print(meta_t)
                
        if meta_s == meta_t:
            return True
        else:
            return False
