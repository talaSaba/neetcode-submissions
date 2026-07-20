class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans=[]
        for i in range(len(nums)):
            s=target-nums[i]
            if s in nums and nums.index(s)!=i:
                ans.append(i)
                ans.append(nums.index(s))
                return sorted(ans)
        return []

