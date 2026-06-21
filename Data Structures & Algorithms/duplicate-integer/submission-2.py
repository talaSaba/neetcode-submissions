class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # nums_counter={}
        # for value in nums:
        #     if value not in nums_counter:
        #         nums_counter[value]=1
        #     else:
        #         return True
        # return False

        # dect={}
        # for i in nums:
        #     dect[i]=dect.get(i,0)+1
        # for i in dect.keys():
        #     if dect[i]>1:
        #         return True
        # return False     


        seen=set()
        for i in nums:
            if i in seen:
                return True
            seen.add(i)
        return False
