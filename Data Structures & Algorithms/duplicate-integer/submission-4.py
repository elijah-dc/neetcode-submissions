class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numbers = set()
        for i in range(len(nums)):
            numbers.add(nums[i])
                
        return len(numbers) != len(nums)