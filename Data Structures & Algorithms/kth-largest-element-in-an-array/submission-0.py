class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        h=[]
        for i in range(len(nums)):
            heapq.heappush(h,(nums[i],i))
            if len(h)>k:
                heapq.heappop(h)
        #arr=[]
        #while h :
        x,y=heapq.heappop(h)
                 
        return x      

        