class Solution:
    def rob(self, nums: List[int]) -> int:
        array=[0]*len(nums)
        if len(nums)==1:
            return nums[0]
        if len(nums)==2:
            return max(nums[0],nums[1])
        array[len(nums)-1]=nums[len(nums)-1]
        array[len(nums)-2]=nums[len(nums)-2]
        for i in range(len(nums)-3,-1,-1):
            array[i]=max(array[i+1],array[i+2]+nums[i])
        return array[0]    
        