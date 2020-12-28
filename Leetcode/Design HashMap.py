# DID NOT PASS ALL TEST CASES

import math

# Hash functions

def hash1(key):
    return int(math.floor(key / 1000))
def hash2(key, hash_key):
    return int(key - hash_key * 1000)

class MyHashMap(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # Initialize Hash Table
        self.table = [[]] * 1000
        for i in range(1000):
            self.table[i].append(-1)
        
        # Use frequency table to keep track of used/unused values
        self.freq_table = {}

    def put(self, key, value):
        """
        value will always be non-negative.
        :type key: int
        :type value: int
        :rtype: None
        """
        
        # Check if value already exists in the table
        try: 
            # Remove original mapping
            # Extract key information
            location = self.freq_table[value]
            # Erase data
            self.table[location[0]][location[1]] = -1
        except KeyError:
            pass
        
        # Run through hash functions to generate keys, and addresses for each value
        hash_key = hash1(key)
        index = hash2(key, hash_key)

        # Install new mapping
        self.table[hash_key][index] = value
        # Store record of value
        self.freq_table[value] = [hash_key, index]
        

    def get(self, key):
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        :type key: int
        :rtype: int
        """
        
        if key == 28:
            print(self.freq_table)
        
        # Run through hash functions to generate keys, and addresses for each value
        hash_key = hash1(key)
        index = hash2(key, hash_key)
        
        return self.table[hash_key][index]
        

    def remove(self, key):
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        :type key: int
        :rtype: None
        """
                
        # Run through hash functions to generate keys, and addresses for each value
        hash_key = hash1(key)
        index = hash2(key, hash_key)
        
        self.table[hash_key][index] = -1


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
