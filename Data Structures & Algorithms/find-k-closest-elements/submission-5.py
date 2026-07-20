class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        h=[]
        for i in range(len(arr)):
            heapq.heappush(h,(abs(arr[i]-x),arr[i]))
            # if len(h)>k:
            #     heapq.heappop(h)

            
        ch=[]
        for i in range(1,k+1):
            x,y=heapq.heappop(h)
            ch.append(y)
        ch.sort()
        return ch