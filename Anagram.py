class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_map = dict()

        # Create a hashmap of the counts of each character
        for char in s:
            if char in s_map:
                s_map[char] += 1
            else:
                s_map[char] = 1
        
        # Iterate through the other string and subtract the counts
        for char in t:
            # if a char is not in the other string it is not a valid anagram
            if char not in s_map:
                return False
            else:
                # If there are more instances of the char in t then it is not a valid anagram
                if s_map[char] <= 0:
                    return False
                s_map[char] -= 1
        
        # Check if any values are not 0
        if sum(s_map.values()) != 0:
            return False
        
        return True




