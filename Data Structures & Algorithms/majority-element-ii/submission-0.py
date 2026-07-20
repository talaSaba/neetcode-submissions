class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # we will do the follow up 
        nums.sort()

        threshold=((len(nums))//3)  
        current=0
        sum=1
        arr=[]
        for i in range(1,len(nums)):
            if nums[current]==nums[i]:
                sum+=1
            else:
                if sum>threshold:
                    arr.append(nums[current])
                current=i
                sum=1
        if sum>threshold:
            arr.append(nums[current])
                      

        return arr
                    

