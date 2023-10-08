class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        out = []
        for row in range(1, numRows + 1):
            if row == 1:
                out.append([1])
            elif row == 2:
                out.append([1,1])
            else:
                toIterate = out[-1]
                toAppend = [1]
                for idx in range(len(toIterate) - 1):
                    toAppend.append(toIterate[idx] + toIterate[idx + 1])
                toAppend.append(1)
                out.append(toAppend)
        
        return out