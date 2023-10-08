class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Set cannot have duplicates
        seen = set()

        for num in nums:
            if num in seen:
                return True
            else:
                seen.add(num)
        
        return False