class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans=[]
        for i in range(len(nums)):
            s=target-nums[i]
            if s in nums and nums.index(s)!=i:
                if i<=nums.index(s):
                    return [i,nums.index(s)]
                return [nums.index(s),i]
                


        return []

