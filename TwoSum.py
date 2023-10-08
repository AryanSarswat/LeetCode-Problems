class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complement = dict()
        for idx in range(len(nums)):
            diff = target - nums[idx]
            if diff in complement:
                return idx, complement[diff]
            else:
                complement[nums[idx]] = idx