from _heapq import heappop
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        has=Counter(tasks)
        heap=[-cnt for cnt in has.values()]
        heapq.heapify(heap)
        q=deque()
        time=0
        while heap or q :
            time+=1
            if heap:
                d=heapq.heappop(heap)+1
                if d!=0:
                    q.append([d,time+n])
            else:
                time=q[0][1]
            if q and q[0][1]==time:
                heapq.heappush(heap,q.popleft()[0])
        return time



        
                

        
