import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #heapppppppppp
        # heap=[]
        # count={}
        # for i in nums:
        #     count[i]=count.get(i,0)+1
        # for key,value in count.items():
        #     heapq.heappush(heap,(value,key))
        #     if len(heap)>k:
        #         heapq.heappop(heap)
        # res=[]
        # while heap:
        #     value,key=heapq.heappop(heap)
        #     res.append(key)
        # return res  
        ########################################################
        #Grouping by the frequiency 
        c=defaultdict(int)
        c_reverse=defaultdict(list)
        for i in range(len(nums)):
          c[nums[i]]+=1
        for key,value in c.items():
          c_reverse[value].append(key)
        res=[]
        for i in range(len(nums), 0, -1):
          for j in range(len(c_reverse[i])):
                res.append(c_reverse[i][j])

                if len(res) == k:
                    return res



             





        
        