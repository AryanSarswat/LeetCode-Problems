class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        map1 = []
        map2 = []

        # Use indexes to do the comparision as even for later string if the first occurance index is same it will lead to true
        for str1 in s:
            map1.append(s.index(str1))
        for str2 in t:
            map2.append(t.index(str2))
        
        return map1 == map2