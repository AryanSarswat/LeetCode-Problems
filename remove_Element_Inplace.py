class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = 0
        for idx in range(len(nums)):
            if nums[idx] == val:
                nums[idx] = 101
                count += 1
        nums.sort()
        return len(nums) - count