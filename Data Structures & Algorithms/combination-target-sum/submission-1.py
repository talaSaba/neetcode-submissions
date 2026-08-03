class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res=[]
        curr=[]
        
        def backtrack(i,n):
            if n>target:
                return 
            if n==target:
                res.append(curr[:])
                return
            if i>=len(nums):
                return
            curr.append(nums[i])
            backtrack(i,n+nums[i])
            #backtrack(i+1,n+nums[i])
            curr.pop()
            backtrack(i+1,n)
            return 
        backtrack(0,0)
        return res

        