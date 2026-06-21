class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxv=0
        l=0
        r=len(heights)-1
        while l<r:
            curr=min(heights[l],heights[r])*(r-l)
            maxv=max(maxv,curr)
            if heights[l]>heights[r]:
                r-=1
            else:
                l+=1
        return maxv            
