class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        heap=[]
        for i in range(len(points)):
            x2,y2=0,0
            x1,y1=points[i][0],points[i][1]
            dist = x1 ** 2 + y1 ** 2
            heapq.heappush(heap,(-1*dist,[x1,y1]))
            if len(heap)>k:
                heapq.heappop(heap)
        res=[]
        while heap:
            dist,lis=heapq.heappop(heap)
            res.append(lis)
        return res
        

        