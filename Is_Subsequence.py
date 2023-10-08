class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # Sanity Check
        if len(s) > len(t):
            return False

        # Exception
        if len(s) == 0:
            return True

        curr_ind = 0
        for ind in range(len(t)):
            if t[ind] == s[curr_ind]:
                curr_ind += 1
            
            if curr_ind >= len(s):
                return True

        return False

