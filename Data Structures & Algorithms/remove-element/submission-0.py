class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        c=len(nums)-1
        write=0
        for read in range(len(nums)):
            if nums[read]==val:
                c-=1

            else:
                nums[write]=nums[read]
                write+=1
        return write


        