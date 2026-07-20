class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if len(nums)==1:
            if nums[0]==target:
                return 1
            else :
                return 0 

        l,r=0,1
        currsum=nums[0]
        minn=float('inf')
        while l<=r and r<len(nums):
            if currsum<target:
                currsum+=nums[r]
                r+=1
                
            else:
                minn=min(minn,r-l)
                while currsum>=target:
                    minn=min(minn,r-l)
                    currsum-=nums[l]
                    l+=1
        # if currsum<target:
        #     return 0             
        while currsum>=target:
            minn=min(minn,r-l)
            currsum-=nums[l]
            l+=1            
        # if minn==len(nums):
        #     return 0 
        # if currsum<target:
        #     return 0 
        if minn==float('inf'):return 0
        return minn         




        