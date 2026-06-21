class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans=[]
        hash=Counter(nums)
        for i in range(len(nums)):
            x=hash[(target-nums[i])];
            if x>0 and i!=nums.index(target-nums[i]):
                return sorted([i,nums.index(target-nums[i])])

        return        []
