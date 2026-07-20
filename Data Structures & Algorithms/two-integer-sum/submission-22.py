class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans=[]
        for i in range(len(nums)):
            s=target-nums[i]
            if s in nums:
                ss=nums.index(s)
                if ss!=i:
                    if i<ss:
                        return [i,ss]
                    return [ss,i]
                


        return []

