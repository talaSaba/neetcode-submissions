class Solution:
    def maxSubArray(self, nums: List[int]) -> int:# maximum subarray ---> this is kadanes algorithem 
        answer=[0]*(len(nums)+1)
        d=float('-inf')
        for i in range(len(nums)-1,-1,-1):
            answer[i]=max(nums[i],answer[i+1]+nums[i])
            d=max(answer[i],d)
        return d 


        