class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans=[]
        for i in range(2*len(nums)):
            ans.append(0)
        for key in range(len(nums)):
            ans[key]=nums[key]
            ans[key+len(nums)]=ans[key]
        return ans    

        