class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # Base case
        if len(arr) <= 1:
            return [-1]
        
        # Create a running counter for the max
        last_max = max(arr[1:])
        arr[0] = last_max
        
        for ind in range(1, len(arr)):
            # it is the last index so we append -1
            if ind == (len(arr) - 1):
                arr[-1] = -1
            else:
                # If the current element is not the last_max we can continue using the last_max
                if arr[ind] != last_max:
                    arr[ind] = last_max
                else:
                    # we have reached the last_max so we need to update it
                    new_max = max(arr[ind+1:])
                    arr[ind] = new_max
                    last_max = new_max
                    
        return arr

        