class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]
        curr=[]
        def back(index):
            if index==len(nums):
                res.append(curr[:])
                return
            else:
                #for i in range(index,len(nums)):
                    curr.append(nums[index])
                    back(index+1)
                    curr.pop()
                    back(index+1)
        back(0)
        return res

        



        