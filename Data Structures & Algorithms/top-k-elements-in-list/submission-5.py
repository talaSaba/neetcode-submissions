import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #heapppppppppp
        heap=[]
        count={}
        for i in nums:
            count[i]=count.get(i,0)+1
        for key,value in count.items():
            heapq.heappush(heap,(value,key))
            if len(heap)>k:
                heapq.heappop(heap)
        res=[]
        while heap:
            value,key=heapq.heappop(heap)
            res.append(key)
        return res  

             





        
        