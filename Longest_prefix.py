class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longestIdx = min([len(i) for i in strs])

        longest_pre = 0
        for i in range(longestIdx):
            flag = True
            chr_cmp = strs[0][i]

            for str in strs[1:]:
                if str[i] == chr_cmp:
                    continue
                else:
                    flag = False
                    break
            
            if flag:
                longest_pre += 1
            else:
                break
        
        return strs[0][:longest_pre]

        