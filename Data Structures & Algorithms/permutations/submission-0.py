class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        cur=[]
        res=[]
        seen=set()
        def back():
            if len(cur)==len(nums):
                res.append(cur[:])
            for x in range(len(nums)):
                if x in seen:
                    continue
                else:
                    seen.add(x)
                    cur.append(nums[x])
                    back()
                    seen.remove(x)
                    cur.pop()
                    
        back()
        return res
                
            
            