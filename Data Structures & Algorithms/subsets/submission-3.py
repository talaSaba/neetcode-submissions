class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        answer=[]
        
        def backtracking(i):
            
            if i == len(nums) :
                answer.append(curr[:])
                return
               
                
            backtracking(i+1)
            curr.append(nums[i])
            backtracking(i+1)
            curr.pop()
                
        
        curr=[]
        backtracking(0)
        return answer    



        