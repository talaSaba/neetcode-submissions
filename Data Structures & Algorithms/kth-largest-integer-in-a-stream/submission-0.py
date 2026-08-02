class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap=[]
        self.k=k
        for i in range(len(nums)):
             heapq.heappush(self.heap,nums[i])
        #heapq.heapify(nums)
        #print((nums))
        while len(self.heap)>k:
            heapq.heappop(self.heap)
        print((self.heap))
        #self.heap=nums
        

        

    def add(self, val: int) -> int:
        j=0
        if len(self.heap)==self.k:
            heapq.heappush(self.heap,val)
            heapq.heappop(self.heap)
            j=self.heap[0]
        else:
            heapq.heappush(self.heap,val)
            j=self.heap[0]
        return  j




        
